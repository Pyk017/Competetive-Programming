/*
 * @lc app=leetcode id=118 lang=cpp
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
#include <bits/stdc++.h>
#include <cmath>
using namespace std;

class Solution
{
public:
    vector<vector<int>> generate(int numRows)
    {
        vector<int> temp = {1};
        vector<vector<int>> result;

        result.push_back(temp);

        if (numRows == 1)
        { //? Base case
            return result;
        }

        temp.push_back(1);
        result.push_back(temp);

        if (numRows == 2)
            return result;

        for (int i = 2; i < numRows; i++)
        {
            vector<int> t(i + 1);
            int mid = floor((i + 1) / 2);
            int j = 0;

            while (j <= mid)
            {
                if (j == 0)
                {
                    t[j] = 1;
                }
                else
                {
                    t[j] = result[i - 1][j] + result[i - 1][j - 1];
                }
                temp[i + 1 - j - 1] = temp[j];
                j -= 1;
            }

            result.push_back(t);
        }

        return result;
    }
};
// @lc code=end
