import json

# 1. 퀴즈 데이터의 틀 (클래스 1)
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

# 2. 퀴즈 게임 관리자 (클래스 2)
class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz("파이썬에서 리스트에 요소를 추가하는 메서드는?", ["add()", "push()", "append()", "insert()"], 3),
            Quiz("파이썬의 창시자는 누구일까요?", ["제임스 고슬링", "귀도 반 로섬", "빌 게이츠", "스티브 잡스"], 2),
            Quiz("정수형 데이터를 의미하는 타입은?", ["str", "int", "float", "bool"], 2),
            Quiz("논리형(True/False) 데이터를 의미하는 타입은?", ["str", "int", "float", "bool"], 4),
            Quiz("출력을 담당하는 파이썬 함수는?", ["input()", "print()", "show()", "display()"], 2)
        ]
        self.best_score = 0

    def show_menu(self):
        print("\n=== 🎯 나만의 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 종료")
        print("==========================")

    def play(self):
        print("\n📝 퀴즈를 시작합니다!")
        score = 0
        for i, q in enumerate(self.quizzes):
            print(f"\n[문제 {i+1}] {q.question}")
            for idx, choice in enumerate(q.choices):
                print(f"{idx+1}. {choice}")
            
            ans = input("정답 입력(번호): ").strip()
            if ans == str(q.answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 {q.answer}번입니다.")
        
        print(f"\n🏆 최종 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        self.save_score(score)

    def save_score(self, score):
        """점수를 'score.json' 파일에 저장하는 기능"""
        data = {"best_score": score}
        with open("score.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("💾 최고 점수가 'score.json'에 저장되었습니다!")
    
    def load_score(self):
        """파일에서 이전 점수를 불러오는 기능"""
        try:
            with open("score.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data["best_score"]
                print(f"📈 이전 최고 점수: {self.best_score}점")
        except FileNotFoundError:
            # 파일이 없으면 그냥 0점으로 시작
            self.best_score = 0

# 3. 실제 게임 실행 부분
game = QuizGame()

while True:
    game.show_menu()
    choice = input("선택: ").strip()

    if choice == "1":
        game.play()
    elif choice == "2":
        print("👋 게임을 종료합니다. 안녕!")
        break
    else:
        print("⚠️ 잘못된 입력입니다. 1번이나 2번을 눌러주세요.")