class Solution:
    def minNumberOfHours(self, init_energy: int, init_exp: int, energy: List[int], experience: List[int]) -> int:
        def check_energy(training):
            e = init_energy + training
            
            for req_e in energy:
                if req_e >= e:
                    return False
                e -= req_e
                
            return True
        
        def check_exp(training):
            exp = init_exp + training
            
            for req_exp in experience:
                if req_exp >= exp:
                    return False
                exp += req_exp
                
            return True
        
        e_training = 0
        exp_training = 0
        
        while not check_energy(e_training):
            e_training += 1
            
        while not check_exp(exp_training):
            exp_training += 1
            
        return e_training + exp_training
