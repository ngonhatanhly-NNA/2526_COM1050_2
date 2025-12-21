import sys

def A():
    line_input = sys.stdin.readline().rstrip().split()
    if not line_input:
        return
    
    line = [int(x) for x in line_input]
    maxi, mini = 0, 0
    check  = [False for _ in range (len(line))]
    for i in range (len(line)):
        if line[i] > line[maxi]:
            check[maxi], check[i] = False, True

            maxi = i
        if line[i] < line[mini]:
            check[mini], check[i] = False, True
            mini = i
    
    if line[maxi] - line[mini] >= 10:
        print('check again')
    else:
        middle = 0
        for i in range (len(line)):
            if not check[i]:
                middle = line[i]
        print(f'final {middle}')

import sys
import math

# Thiết lập I/O nhanh hơn cho các bài toán competitive programming
# Bằng cách sử dụng sys.stdin.readline
"""Khong biet lam T^T"""
def B_final_fix(): # K bieets lamf T^T 
    # Đọc dòng tham số đầu tiên
    try:
        # Sử dụng sys.stdin.readline() thay vì input() để đọc nhanh hơn
        n_input = sys.stdin.readline().strip().split()
        if not n_input: return
        buses, people, road, bus_speed, walking_speed = map(int, n_input)
    except:
        return

    # 1. Đọc và lưu trữ vị trí của các bus
    bus_segments = []
    points = {0, road}
    
    for _ in range(buses):
        line = sys.stdin.readline().strip().split()
        if not line: break
        
        try:
            s_i, t_i = map(int, line)
            if s_i < t_i and s_i <= road:
                 bus_segments.append((s_i, t_i))
                 points.add(s_i)
                 points.add(t_i)
        except:
            continue
    
    # Sắp xếp và lọc các điểm quan trọng (s_i, t_i, 0, road)
    sorted_points = sorted([p for p in points if 0 <= p <= road])
    point_to_idx = {p: i for i, p in enumerate(sorted_points)}
    num_points = len(sorted_points)
    
    # DP array: T[i] = min time from sorted_points[i] to road
    # Khởi tạo với thời gian đi bộ toàn bộ
    T = [(road - sorted_points[i]) / walking_speed for i in range(num_points)]
    T[point_to_idx[road]] = 0.0 # T[road] = 0

    # 2. Dynamic Programming (Lặp ngược từ road về 0)
    for i in range(num_points - 2, -1, -1):
        curr_pos = sorted_points[i]
        
        # Xem xét tất cả các tuyến bus có thể bắt đầu từ curr_pos hoặc xa hơn
        for s_i, t_i in bus_segments:
            if s_i >= curr_pos:
                
                if t_i in point_to_idx:
                    t_idx = point_to_idx[t_i]
                    
                    # 1. Thời gian đi bộ từ curr_pos đến s_i
                    time_walk_to_start = (s_i - curr_pos) / walking_speed
                    
                    # 2. Thời gian đi bus từ s_i đến t_i
                    time_bus_ride = (t_i - s_i) / bus_speed
                    
                    # Tổng thời gian qua tuyến bus này: Walk + Bus + MinTime_from_t_i
                    total_time_via_bus = time_walk_to_start + time_bus_ride + T[t_idx]
                    
                    # Cập nhật DP: T[i] là thời gian tối thiểu
                    T[i] = min(T[i], total_time_via_bus)

    # 3. Xử lý truy vấn của từng người
    results = []
    for _ in range(people):
        try:
            # Đọc vị trí người dân, đảm bảo dùng sys.stdin.readline
            pos_line = sys.stdin.readline().strip()
            if not pos_line: break
            pos = int(pos_line)
        except: break

        if pos >= road:
            results.append(0.0)
            continue
            
        # Vị trí pos của người dân không nhất thiết là một điểm quan trọng.
        # Phải tính toán lại dựa trên các giá trị DP đã có.
        
        # Khởi tạo với thời gian đi bộ toàn bộ
        min_time_from_pos = (road - pos) / walking_speed 

        # Lặp qua tất cả các bus mà người này có thể bắt kịp
        for s_i, t_i in bus_segments:
            if s_i >= pos:
                if t_i in point_to_idx:
                    t_idx = point_to_idx[t_i]
                    
                    # Tính thời gian tương tự như trong DP, nhưng xuất phát từ 'pos'
                    time_walk_to_start = (s_i - pos) / walking_speed
                    time_bus_ride = (t_i - s_i) / bus_speed
                    
                    # Min time from t_i to road is T[t_idx]
                    total_time_via_bus = time_walk_to_start + time_bus_ride + T[t_idx]
                    
                    min_time_from_pos = min(min_time_from_pos, total_time_via_bus)
                    
        results.append(min_time_from_pos)

    # In kết quả
    sys.stdout.write('\n'.join(f"{t:.10f}" for t in results) + '\n')

from itertools import permutations
def E():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)

    n = int(next(it))
    for _ in range(n):
        num = next(it)
        arr = list(num)
        
        res = ["".join(p) for p in permutations(arr)]
        length = len(res)
        first = (int(next(it)) - 1) % length
        second = (int(next(it)) - 1) % length
        
        similar = 0
        for i in range (len(arr)):
            if res[first][i] == res[second][i]:
                similar += 1
            
        print(f"{similar}A{len(arr) - similar}B")
import math
def F():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)
    # Cho các server, tìm tổng chi phí bé nhất, có thể thực hiện vô số kết nôi
    # Nhứng phải đáp ứng các server dều được kết nối với nhau, trực tiêp hoặc không trực tiếp
    # Chi phí là gcd giữa 2 server 
    # Sẽ luôn phải có sever link vs nhau
    # Kiêu như được lựa chọn kết nối, nhưng khi nối index 1 với 3 thì phải qua chi phí là gcd của cả 1, 2, 3
    # Tương tự ta chia nhỏ thành 2 kết nối lớn nối với nhau từ xuôi và ngược
    # gcd(1->3) gcd(3-> 4)
    n = int(next(it))
    arr = [int(next(it)) for _ in range (n)]
    # Requires gcd from index i to index n
    left, right = [0] * n, [0] * n
    # Prefix GCD
    left[0] = arr[0]
    for i in range (1, n):
        left[i] = math.gcd(left[i-1], arr[i])
    # Suffix GCD
    right[n-1] = arr[n-1]
    for i in range (n-2, -1, -1):
        right[i] = math.gcd(right[i+1], arr[i])
    # Lấy giá trị của gcd left -1 coi như điểm chọn cuối , thì khi cộng, bao quat đc các gcd?
    # thì ta có chi phí của 1 -> cuối, còn tìm chi phí của 1 _> các gt ỏ cuois -> các gtri
    # gcd càng nhiều số thì càng nhỏ, vì vậy tối ưu nhất của gcd đầu đến cuối là mã dãy
    ans = left[n-1]
    for i in range (1, n-1):
        ans += min(left[i], right[i])

    print(ans)

if __name__ == "__main__":
    F()
    