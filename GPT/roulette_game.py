import tkinter as tk
import random
import time

def spin_roulette():
    spin_button.config(state=tk.DISABLED)
    result_label.config(text="Spinning...")
    root.update()
    
    for _ in range(30):  # 애니메이션처럼 보이도록 여러 번 이름 변경
        current_winner = random.choice(players)
        result_label.config(text=f"{current_winner} 🎯")
        root.update()
        time.sleep(0.1)
    
    final_winner = random.choice(players)
    result_label.config(text=f"Winner: {final_winner} 🎉")
    spin_button.config(state=tk.NORMAL)

# GUI 설정
root = tk.Tk()
root.title("2-Player Roulette")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# 제목
title_label = tk.Label(root, text="2-Player Roulette", font=("Arial", 20), bg="#f0f0f0")
title_label.pack(pady=10)

# 플레이어 입력
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

player1_label = tk.Label(frame, text="Player 1:", font=("Arial", 12), bg="#f0f0f0")
player1_label.grid(row=0, column=0, padx=10, pady=5)
player1_entry = tk.Entry(frame, font=("Arial", 12))
player1_entry.grid(row=0, column=1, pady=5)

player2_label = tk.Label(frame, text="Player 2:", font=("Arial", 12), bg="#f0f0f0")
player2_label.grid(row=1, column=0, padx=10, pady=5)
player2_entry = tk.Entry(frame, font=("Arial", 12))
player2_entry.grid(row=1, column=1, pady=5)

# 결과 표시
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0")
result_label.pack(pady=20)

# 버튼
def start_game():
    global players
    players = [player1_entry.get(), player2_entry.get()]
    if len(players[0]) > 0 and len(players[1]) > 0:
        spin_button.pack(pady=10)
        result_label.config(text="Press Spin to Start!")
    else:
        result_label.config(text="Please enter both names!")

start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game, bg="#4CAF50", fg="white", width=15)
start_button.pack(pady=10)

spin_button = tk.Button(root, text="Spin Roulette", font=("Arial", 12), command=spin_roulette, bg="#2196F3", fg="white", width=15)
spin_button.pack_forget()

# GUI 실행
root.mainloop()
