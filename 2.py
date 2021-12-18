nums = [] # あとに行くほど未来
length = int(input()) # 時系列データ(配列)の長さを受け付ける
for _ in range(length):
  inputted = input()
  nums.append(int(inputted))

# jより前の値の中で、最小値をminvに格納しておく
minv = nums[0] # 初期化
maxv = -1 * 1e9
for j in range(1, length):
  maxv = max(maxv, nums[j] - minv)
  minv = min(minv, nums[j])
  
print(maxv)