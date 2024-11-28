#def format_name(f_name, l_name):
 #   print( f_name.title())
  #  print( l_name.title())
   
        


#format_name("amantia", "FANARA")

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    
year = int(input("enter year: "))
answer= is_leap_year(year)
print(answer)



"""def is_leap_year(year):
    
    #Return True if the given year is a leap year, False otherwise.
    
    # Check if the year is divisible by 400
    if year % 400 == 0:
        return True
    # Check if the year is divisible by 100 but not by 400
    elif year % 100 == 0:
        return False
    # Check if the year is divisible by 4 but not by 100
    elif year % 4 == 0:
        return True
    # If none of the above conditions are met, it's not a leap year
    else:
        return False

# Example usage:
year = int(input("Enter a year: "))
print(is_leap_year(year))"""