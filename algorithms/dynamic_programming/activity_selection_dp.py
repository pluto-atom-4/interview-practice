"""
Dynamic Programming approach to the Activity Selection Problem.

"""
def select_activities_dp(activities):
    activities = sorted(activities, key=lambda x: x[0])
    n = len(activities)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if activities[j][1] <= activities[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_count = max(dp)
    selected = []
    end_time = float('inf')
    for i in reversed(range(n)):
        if dp[i] == max_count and activities[i][1] <= end_time:
            selected.append(activities[i])
            end_time = activities[i][0]
            max_count -= 1
    return selected[::-1]
