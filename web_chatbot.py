"""
Flask 기반 웹 챗봇 서버

주요 기능:
1. 웹 UI 제공 (/, /logs)
2. 채팅 API (/api/chat)
3. 미답변 질문 조회 API (/api/unanswered)
4. 서버 상태 확인 API (/api/health)

실행 방법:
    py -3.11 web_chatbot.py
    
접속 URL:
    http://localhost:5000 (메인)
    http://localhost:5000/logs (로그)
"""
from flask import Flask, render_template, request, jsonify, send_from_directory
from rag_chatbot_v2 import SemanticRAGChatbot
import logging
import os

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask 앱 생성
app = Flask(__name__)

# 전역 챗봇 인스턴스
chatbot = None

def initialize_chatbot():
    """
    챗봇 초기화 함수
    
    기능:
        1. SemanticRAGChatbot 인스턴스 생성
        2. data/data.xlsx 파일 로딩
        3. 각 질문에 대한 임베딩 생성 (로컬 모델 - 한국어 특화)
        4. 메모리에 임베딩 저장
    
    Raises:
        Exception: 초기화 실패 시
    """
    global chatbot
    try:
        logger.info("챗봇 초기화 중...")
        # RAG 챗봇 생성 (enable_logging=True: 미답변 질문 자동 로깅)
        chatbot = SemanticRAGChatbot('./data/data.xlsx')
        logger.info("챗봇 초기화 완료")
    except Exception as e:
        logger.error(f"챗봇 초기화 실패: {str(e)}")
        raise

@app.route('/')
def index():
    """
    메인 챗봇 페이지
    
    Returns:
        HTML: templates/index.html 렌더링
    """
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    채팅 API 엔드포인트
    
    Request JSON:
        {
            "question": "사용자 질문"
        }
    
    Response JSON:
        {
            "success": true/false,
            "answer": "답변 내용" (성공 시)
            "error": "오류 메시지" (실패 시)
        }
    
    Process:
        1. 사용자 질문 받기
        2. 의미 검색으로 유사한 질문-답변 찾기
        3. 가장 유사한 답변 반환
        4. 못 찾으면 자동 로깅
    """
    try:
        # JSON 데이터에서 질문 추출
        data = request.get_json()
        question = data.get('question', '').strip()
        
        # 빈 질문 체크
        if not question:
            return jsonify({
                'success': False,
                'error': '질문을 입력해주세요.'
            })
        
        # 챗봇으로 답변 생성
        # - 의미 검색으로 유사한 질문 찾기
        # - 엑셀 데이터의 답변 그대로 반환
        answer = chatbot.generate_answer(question)
        
        # 성공 응답
        return jsonify({
            'success': True,
            'answer': answer
        })
        
    except Exception as e:
        # 오류 로깅 및 응답
        logger.error(f"채팅 오류: {str(e)}")
        return jsonify({
            'success': False,
            'error': f'오류가 발생했습니다: {str(e)}'
        })

@app.route('/api/health')
def health():
    """
    서버 상태 확인 API
    
    Returns:
        JSON: {
            "status": "ok",
            "knowledge_base_size": 27
        }
    
    용도: 서버가 정상 작동하는지 확인
    """
    return jsonify({
        'status': 'ok',
        'knowledge_base_size': len(chatbot.knowledge_base) if chatbot else 0
    })

@app.route('/api/unanswered')
def get_unanswered():
    """
    미답변 질문 목록 조회 API
    
    Returns:
        JSON: {
            "success": true,
            "total": 전체 로그 수,
            "unanswered_count": 미답변 질문 수,
            "questions": [...] 질문 리스트
        }
    
    Process:
        1. 임시 파일 병합 시도 (엑셀 열린 상태 대응)
        2. logs/unanswered_questions.xlsx 읽기
        3. JSON으로 변환하여 반환
    """
    try:
        if chatbot and chatbot.enable_logging:
            # 임시 파일이 있으면 엑셀에 병합
            # (관리자가 엑셀 닫은 후 자동 병합)
            chatbot.question_logger.merge_temp_file()
            
            # 모든 로그된 질문 조회
            df = chatbot.question_logger.get_all_questions()
            
            # DataFrame을 JSON으로 변환
            questions = df.to_dict('records')
            
            # 성공 응답
            return jsonify({
                'success': True,
                'total': len(questions),
                'unanswered_count': chatbot.question_logger.get_unanswered_count(),
                'questions': questions
            })
        else:
            return jsonify({
                'success': False,
                'error': '로깅이 비활성화되어 있습니다.'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/logs')
def logs_page():
    """
    로그 조회 웹 페이지
    
    Returns:
        HTML: templates/logs.html 렌더링
        
    기능:
        - 미답변 질문 목록 표시
        - 실시간 통계 (전체/미답변/완료)
        - 5초마다 자동 새로고침
    """
    return render_template('logs.html')

@app.route('/logo')
def serve_logo():
    """
    KTR 로고 이미지 제공
    
    Returns:
        Image: ktr로고.png 파일
    """
    return send_from_directory('.', 'ktr로고.png')

if __name__ == '__main__':
    # 1. 챗봇 초기화
    # - data/data.xlsx 로딩
    # - 27개 질문에 대한 임베딩 생성 (로컬 모델)
    initialize_chatbot()
    
    # 2. 서버 시작 안내 출력
    print("\n" + "="*60)
    print("Chat KTR 서버 시작")
    print("="*60)
    print("URL: http://localhost:5000")
    print("지식 베이스: {}개 질문-답변".format(len(chatbot.knowledge_base)))
    print("의미 기반 검색 활성화")
    print("="*60 + "\n")
    
    # 3. Flask 웹 서버 실행
    # - host='0.0.0.0': 네트워크 모든 주소에서 접속 가능
    # - port=5000: 5000번 포트 사용
    # - debug=True: 코드 수정 시 자동 재시작
    app.run(host='0.0.0.0', port=5000, debug=True)
