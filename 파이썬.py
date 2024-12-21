import os
import matplotlib.pyplot as plt
import numpy as np

# 상자의 크기 및 구슬의 위치 설정
box_size = 10  # 상자의 한 변의 길이
ball_positions = np.array([[5, 5]])  # 구슬의 위치, 상자의 중앙

# 이미지를 저장할 폴더 경로 설정
image_folder = "E:\\파이썬 테스트\\레이트레이싱\\images"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 결과 이미지 저장을 위한 파일 경로 포맷 설정
image_path_format = os.path.join(image_folder, "light_simulation_{angle}.png")

# 각도에 따른 빛의 원점 위치 계산 및 시각화
angles = np.linspace(0, 2 * np.pi, 360)
for angle in angles:
    light_source_x = box_size / 2 + box_size * np.cos(angle)
    light_source_y = box_size / 2 + box_size * np.sin(angle)

    fig, ax = plt.subplots()
    ax.plot(ball_positions[:,0], ball_positions[:,1], 'o', color='blue')  # 구슬 위치 표시
    ax.plot(light_source_x, light_source_y, '*', color='yellow')  # 빛의 원점 표시
    for ball_pos in ball_positions:
        ax.plot([light_source_x, ball_pos[0]], [light_source_y, ball_pos[1]], color='red')  # 빛의 경로 표시
    
    ax.set_xlim(0, box_size)
    ax.set_ylim(0, box_size)
    ax.axis('off')

    plt.savefig(image_path_format.format(angle=int(np.degrees(angle))))
    plt.close()
