class FamilyTripPlanner:
    def __init__(self, destination, start_date, end_date):
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.members = []
        self.itinerary = {}

    def add_member(self, name, role, notes=""):
        """여행 멤버와 특이사항(예: 선호도, 체력 고려사항)을 추가합니다."""
        self.members.append({"name": name, "role": role, "notes": notes})

    def add_schedule(self, date, time_slot, activity, location, pace="보통"):
        """
        일정을 추가합니다. 
        pace(일정 강도)를 넣어 아이나 어르신이 무리하지 않도록 체크합니다.
        """
        if date not in self.itinerary:
            self.itinerary[date] = []
        
        self.itinerary[date].append({
            "time_slot": time_slot,
            "activity": activity,
            "location": location,
            "pace": pace # 여유로움, 보통, 강행군
        })

    def display_summary(self):
        """전체 여행 요약과 일정을 출력합니다."""
        print("=" * 40)
        print(f"🌴 {self.destination} 가족 여행 플래너 🌴")
        print(f"📅 일정: {self.start_date} ~ {self.end_date}")
        print("=" * 40)
        
        print("\n👥 [참석자 명단 및 참고사항]")
        for m in self.members:
            print(f" - {m['role']} ({m['name']}): {m['notes']}")
            
        print("\n🗓️ [일정표]")
        for date, plans in self.itinerary.items():
            print(f"\n[{date}]")
            for plan in plans:
                print(f" ⏰ {plan['time_slot']} | {plan['activity']} (@{plan['location']}) - 강도: {plan['pace']}")
        print("=" * 40)


# --- [프로그램 실행 예시] ---

# 1. 여행 기본 정보 세팅
trip = FamilyTripPlanner(
    destination="호주 브리즈번 & 골드코스트", 
    start_date="2026-10-17", 
    end_date="2026-10-24"
)

# 2. 참석 가족 구성원 등록 (체력 및 선호도 고려)
trip.add_member("본인", "총괄 기획", "운전 및 전체 동선 관리")
trip.add_member("어머니", "VIP", "무리한 걷기 지양, 여유로운 풍경 감상 선호")
trip.add_member("아내", "재무/서포트", "맛집 탐방 및 카페 휴식")
trip.add_member("딸", "활력소", "동물원, 테마파크, 물놀이 필수")
trip.add_member("남동생", "액티비티", "운전 교대, 활동적인 일정 선호")
trip.add_member("사촌", "자유 영혼", "개별 자유 시간 배려")

# 3. 주요 일정 및 동선 기획
# 10월 17일: 도착 및 적응
trip.add_schedule("2026-10-17", "오전", "공항 도착 및 렌터카 픽업", "브리즈번 공항", "보통")
trip.add_schedule("2026-10-17", "오후", "숙소 체크인 및 인근 산책", "사우스뱅크", "여유로움")

# 10월 18일: 아이와 어른이 모두 만족하는 일정
trip.add_schedule("2026-10-18", "오전", "코알라/캥거루 만나기", "론 파인 코알라 보호구역", "보통")
trip.add_schedule("2026-10-18", "오후", "골드코스트로 이동 (약 1시간)", "렌터카 이동", "여유로움")
trip.add_schedule("2026-10-18", "저녁", "해변 야경 감상 및 가족 식사", "서퍼스 파라다이스", "여유로움")

# 4. 결과 출력
trip.display_summary()