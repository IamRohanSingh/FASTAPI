if __name__ == "__main__":
    def string_cal_lenght(my_string):
        count = 0
        for _ in my_string:
            count += 1
        return count

    def generate_string(lenght):
        string = ''
        while lenght>0:
            string += input()
            lenght -= 1
        return string    
        

