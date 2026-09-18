class Solution(object):
    def maximumWealth(self, accounts):
        richest_person = 0
        for account in accounts:
            account_total = sum(account)
            if account_total > richest_person:
                richest_person = 0 + account_total
        return richest_person 
