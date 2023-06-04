import googlemaps
import polyline

# Google Maps API 키를 입력하세요.
api_key = 'AIzaSyAQ5aElKgEv8I0Bz1cVG7lVvmMhalRr-Vg'

# 시작점과 도착점의 좌표를 입력하세요.
start = (37.7749, -122.4194)  # 예시 좌표 (샌프란시스코)
end = (34.0522, -118.2437)  # 예시 좌표 (로스앤젤레스)

# Google Maps 클라이언트를 생성합니다.
gmaps = googlemaps.Client(key=api_key)

# 높이 프로파일 데이터를 가져옵니다.
elevation_data = gmaps.elevation_along_path(polyline.encode([start, end]), samples=100)

# 높이 정보를 추출하여 리스트에 저장합니다.
elevation_list = [point['elevation'] for point in elevation_data]

# 결과를 출력합니다.
print(elevation_list)
