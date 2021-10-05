class Time:

    def __init__(self, h, m, s):
        self.hours = h
        self.mins = m
        self.secs = s

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.mins

    def getSeconds(self):
        return self.secs
    """
    toString
    returns a string representing the time in hr : min : sec form
    @return a string representing the time in hr : min : sec form
    """
    def toString(self):
        return str(self.hours) + " hrs : " + str(self.mins) + " mins : " + str(self.secs) + " seconds "
    """
    timeInSeconds
    returns the Time in seconds
    @return the about of seconds equivalent to the time 
    """
    def timeInSeconds(self):
        return 3600 * self.hours + 60 * self.mins + self.secs

    """
    changeTheTime
    changes the time to what is inputted
    @param h the new hours
    @param m the new minutes
    @param s the new seconds
    """
    def changeTheTime(self, h, m, s):
        self.hours = h
        self.mins = m
        self.secs = s

    """
    twelveHourClock
    returns the time in 12 hr format
    @return the time in 12 hr form with am or pm at the end
    """
    def twelveHourClock(self):
        if self.hours > 12:#if after 12 returns time as pm if before returns it as am
            return str(self.hours-12) + " hours : " + str(self.mins) + " minutes : " + str(self.secs) + " seconds pm"
        elif self.hours == 12:
            return self.toString() + "pm"
        else:
            return self.toString() + "am"

    """
    whatTimeIsIt 
    returns the general time of day the time falls under
    @return the general time of day the time falls under(morning,afternoon,evening or nightime)
    """
    def whatTimeIsIt(self):
        if self.hours >= 6 and self.hours < 12:#returns the time of day based on hours
            return "morning"
        elif self.hours >= 12 and self.hours < 17:
            return "afternoon"
        elif self.hours >= 17 and self.hours < 22:
            return "evening"
        else:
            return "nightime"
    """
    compareTo
    returns the amount of seconds between two time objects
    @param t the explicit time parameter
    @return the seconds between two time objects
    """
    def compareTo(self, t ):
        return self.timeInSeconds() - t.timeInSeconds()
    """
    timeTill
    returns a time object that is the time between two other time objects
    @param t the explicit time parameter in the future
    @return the time object between the explicit and implicit time parameters
    """
    def timeTill(self, t):
        h = t.compareTo(self)//3600
        m = (t.compareTo(self)%3600)//60
        s = (t.compareTo(self)%60)

        timeTill = Time(h,m,s)
        return timeTill


