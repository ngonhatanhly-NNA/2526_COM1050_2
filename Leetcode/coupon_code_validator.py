from collections import List
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # The coupon is considered valid only when it consits only character and dgit and underscore, else not valid
        # The coupon is considered valid onlt when itis still activated
        business_Codes = list(zip(businessLine, code, isActive))
        # Attention, zip only a method to link, not have saving funciton
        business_Codes.sort(key = lambda x: (x[0], x[1]))
        name = {"electronics", 'grocery', 'pharmacy', 'restaurant'}
        res = []
        for business, voucher, active in business_Codes:
            validate = True
            if (business not in name) or (not active) or (not voucher):
                validate = False
            
            if validate:
                for c in voucher:
                    is_valid_char = c.isalnum() or c == '_'
                    if not is_valid_char:
                        validate = False
                        break
            if validate:
                res.append(voucher)

        return res
        