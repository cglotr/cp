class Solution:
    def minNumberOfHours(self, init_ene, init_exp, energy, experience):
        ans = 0
        
        for r_ene, r_exp in zip(energy, experience):
            if init_ene <= r_ene:
                ans += r_ene - init_ene + 1
                init_ene = r_ene + 1
                
            if init_exp <= r_exp:
                ans += r_exp - init_exp + 1
                init_exp = r_exp + 1
                
            init_ene -= r_ene
            init_exp += r_exp
        
        return ans
