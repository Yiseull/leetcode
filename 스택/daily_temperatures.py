class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, answer = [], [0] * len(temperatures)

        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and temperatures[stack[-1]] < cur:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer