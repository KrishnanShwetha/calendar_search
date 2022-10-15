
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        
        self.month=init_month
        self.day=init_day
        self.year=init_year


    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date


    #part 3
    def advance_one(self):
        """advance_one(self) that changes the called object so that 
        it represents one calendar day after the date that it originally represented.
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # to check if we should go to the next year
        if self.day + 1 > days_in_month[self.month] and self.month == 12:
            self.month = 1
            self.day = 1
            self.year += 1
        # to check if it is a leap year
        elif self.day + 1 > days_in_month[self.month] and self.is_leap_year() == True and self.month == 2 and self.day < 29:
            self.day += 1
        # to check if the month should be incremented
        elif self.day + 1 > days_in_month[self.month]:
            self.month += 1 
            self.day = 1
        # to just increment the day by one
        else:
            self.day += 1
        
    # Part 4
    def advance_n(self, n):
        """advance_n(self, n) that changes the calling object so that 
        it represents n calendar days after the date it originally 
        represented. Additionally, the method should print all of the 
        dates from the starting date to the finishing date, inclusive of 
        both endpoints.
        """
        print(self)
        for day in range(n):
            self.advance_one()
            print(self)
    
    # Part 5
    def __eq__(self, other):
        """__eq__(self, other) that returns True if the called object (self) 
        and the argument (other) represent the same calendar date 
        (i.e., if the have the same values for their day, month, and 
         year attributes). Otherwise, this method should return False.

        """
        if self.day==other.day and self.month==other.month and self.year==other.year:
            return True
        else:
            return False
        
    #Part 6
    def is_before(self, other):
        """is_before(self, other) that returns True if the called object 
        represents a calendar date that occurs before the calendar 
        date that is represented by other. If self and other represent 
        the same day, or if self occurs after other, the method should 
        return False.
        """
        # first check year
        if self.year > other.year:
            return False
        elif self.year < other.year:
            return True
        # months in the same year
        if self.month > other.month:
            return False
        elif self.month < other.month:
            return True
        # days in the same month
        if self.day > other.day:
            return False
        elif self.day < other.day:
            return True
        # same day
        elif self.day == other.day and self.month == other.month:
            
            return False
        

        
    # Part 7
    def is_after(self, other):
        """is_after(self, other) that returns True if the calling object 
        represents a calendar date that occurs after the calendar date 
        that is represented by other. If self and other represent the 
        same day, or if self occurs before other, the method should return False.
        """
        if self.__eq__(other) == True:
            return False
        elif self.is_before(other) == True:
            return False
        else:
            return True
    
    # Part 8
    def days_between(self,other):
        """days_between(self, other) that returns an integer that represents 
        the number of days between self and other.
        """
        self_date = self.copy()
        other_date = other.copy()
        
        
        num_days_btw = 0
        if self.__eq__(other) == True:
            num_days_btw = 0
            
        elif self.is_before(other) == True:
            
            while self_date.is_before(other_date) == True:
                self_date.advance_one()
                num_days_btw -= 1
            
        elif self.is_before(other) == False:
            
            while self_date.is_after(other_date) == True:
                other_date.advance_one()
                num_days_btw += 1
        
        return num_days_btw 

      
        
    
    # Part 9
    def day_name(self):
        """day_name(self) that returns a string that indicates the name of 
        the day of the week of the Date object that calls it. In other words, 
        the method should return one of the following strings: 'Monday', 'Tuesday', 
        'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'.
        """
        week_days = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        known_date=Date(11, 11, 2019)
        days_btw=self.days_between(known_date)
        day_name_index=days_btw%7
        day_name=week_days[day_name_index]
        return day_name
    
    
        
        
        
    
        
        
        
            
    
            
        
