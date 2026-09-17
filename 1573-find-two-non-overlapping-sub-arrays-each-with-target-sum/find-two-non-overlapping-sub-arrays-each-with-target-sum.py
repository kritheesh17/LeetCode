class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = shortest valid subarray
        # completely inside arr[0...i]
        best = [float('inf')] * n

        prefix = 0
        prefix_index = {0: -1}

        ans = float('inf')
        min_len = float('inf')

        for i in range(n):
            prefix += arr[i]

            # If prefix - target existed,
            # then arr[j+1 ... i] has sum = target.
            if prefix - target in prefix_index:
                j = prefix_index[prefix - target]
                length = i - j

                # Combine with the shortest previous subarray
                if j >= 0 and best[j] != float('inf'):
                    ans = min(ans, length + best[j])
                elif j == -1:
                    # No previous subarray exists
                    pass

                min_len = min(min_len, length)

            # Store shortest valid subarray ending at/before i
            best[i] = min_len

            # Store earliest occurrence of prefix sum
            if prefix not in prefix_index:
                prefix_index[prefix] = i

        return -1 if ans == float('inf') else ans