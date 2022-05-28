#Stats.py
#List the 25, top 3 times, top 3 first names, the average time, and the top finishers time and full name from a list of 25 finishers from a HS race.
def main():

    infile = open("input.txt", 'r')
    outfile = open("output.txt", "w")

    topfinishername = "" #Setting to empty string to use for later
    topfinishertime = "" 
    finishinglist = [] #Empty list for finishing times
    top3names = [] 

    for line in infile: #Read the file 
        words = [] #Empty list to have the ability to add to it 
        finishinglist.append(float(line.split()[3])) #Add times to the list
        finishinglist.sort() #Sort in order from fastest to slowest

        if topfinishername == "": #Check to see if fastest name is empty, then set it to the first finsiher
            topfinishername = line.split()[1] + " " + line.split()[2] #First name and Last name 
            topfinishertime = line.split()[3] #Time

        elif line.split()[3] < topfinishertime: #If a new time is faster, set that as the top time
            topfinishername = line.split()[1] + " " + line.split()[2] 
            topfinishertime = line.split()[3] 

        top3names.append(line.split()[1]) #Add names to the top three names list


    average = (sum(finishinglist)) / 25 #Find the average time

    print("Here are some statistics on the Top 25 Finishers from the FSHAA 2A Region 3 Girl's 5k race:", file=outfile)
    
    print("\n5k times in order of finishing time:", file=outfile) 
    for a in finishinglist:
        print(a, file=outfile) #Print the list in order of finishing time
    
    print("\nThe top three times from this race are: ", file=outfile)
    for i in range(0, 3):
        print(finishinglist[i], file=outfile) #Print only top 3

    print("\nThe top three indivual first names are:", file=outfile)#Print the top three finishers
    for i in range(0, 3):
        print(top3names[i], file=outfile) #Print only top 3 names
    
    print("\nThe average time between finishers is:", "{:.2f}".format(average), "minutes", file=outfile) #Print the average times

    print("\nThe top finisher:", topfinishername, file=outfile) #Print the fastest person
    print(topfinishername + "'s", "5k time was:",topfinishertime, file=outfile)

    infile.close()
    outfile.close()

 
if __name__ == "__main__":
    main()