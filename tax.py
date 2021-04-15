
def interface():
    # show selection for single or married first
    #let them type income
    # return income, mpf, tax (lowest)
    run = True
    print("@"*50)
    h = 3
    for i in range(h):
        if i+1 == int(h-1/2):
            print(("@"+" "*17+"Tax calculator"+" "*17+"@"))
        else:
            print("@"*7+" "*18+" "*18+"@"*7)
    print("@" * 50)
    while run:
        print("Select Marital status (Type number to select)")
        print("1    Single")
        print("2    Married")
        s = False
        s2 = 0
        s3 = False
        while not s:
            status = input()
            if status == "1":
                status = 1
                s = True
            elif status == "2":
                status = 2
                s = True
            else:
                print("Invalid selection, please select again.")
        while s2 != 2:
            while s2 < 1:
                self = input("please input self yearly income: ")
                try:
                    self = int(self)
                    if self < 0:
                        print("Invalid input, please try again.")
                    else:
                        if status == 1:
                            s2 = 2
                        else:
                            s2 = 1
                except:
                    print("Invalid input, please try again.")
            while s2 < 2:
                spouse = input("please input spouse yearly income: ")
                try:
                    spouse = int(spouse)
                    if spouse < 0:
                        print("Invalid input, please try again.")
                    else:
                        s2 = 2
                except:
                    print("Invalid input, please try again.")

            if status == 2:
                income = [self, spouse]
            else:
                income = self

            r = cal(status, income)
            if status == 1:
                if r[0] == "pr":
                    taxmsg = "Progressive Rate Tax: "
                else:
                    taxmsg = "Standard Rate Tax: "
                print("@"*50)
                print("Yearly Income: " + str(r[1]))
                print("")
                print("MPF: " + str(r[2]))
                print("")
                print(taxmsg + str(int(r[3])))
            else:
                if r[0] == "pr":
                    taxmsg = "Separate Assessment Progressive Rate Tax: "
                elif r[0] == "sr":
                    taxmsg = "Separate Assessment Standard Rate Tax: "
                elif r[0] == "jpr":
                    taxmsg = "Joint Assessment Progressive Rate Tax: "
                else:
                    taxmsg = "Joint Assessment Standard Rate Tax: "
                if "j" in r[0]:
                    print("@"*50)
                    print("JointYearly Income: " + str(r[1]))
                    print("")
                    print("Joint MPF: " + str(r[2]))
                    print("")
                    print(taxmsg + str(int(r[3])))
                else:
                    print("@"*50)
                    print("Self Yearly Income: " + str(r[1]))
                    print("Spouse Yearly Income: " + str(r[3]))
                    print("Self MPF: " + str(r[2]))
                    print("Spouse MPF: "+ str(r[4]))
                    print(taxmsg + str(int(r[5])))
        print("Back to Start? y/n")
        while not s3:
            f = input()
            if f == "y":
                s3 = True
            elif f == "n":
                run = False
                s3 = True
            else:
                print("Invalid choice, please type again. y/n")

def cal(status, income):
    if status == 1:
        singlei = income
        mpf = int(singlei * 0.05)
        if singlei < 85200:
            mpf = 0
        elif mpf > 18000:
            mpf = 18000
        ni = singlei - mpf
        nci = ni - 132000
        if nci < 0:
            nci = 0
        # progressive rate
        if nci <= 50000:
            pr1 = nci * 0.02
        elif nci <= 100000:
            pr1 = 50000 * 0.02 + (nci - 50000) * 0.06
        elif nci <= 150000:
            pr1 = 50000 * 0.02 + 50000 * 0.06 + (nci - 100000) * 0.1
        elif nci <= 200000:
            pr1 = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + (nci - 150000) * 0.14
        elif nci > 200000:
            pr1 = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (nci - 200000) * 0.17
        # standard rate
        sr1 = ni * 0.15
        pr = ["pr", singlei, mpf, int(pr1)]
        sr = ["sr", singlei, mpf, int(sr1)]
        a = [pr, sr]
        a.sort(key=lambda x: x[-1])
        return a[0]
    else:
        bigpr = []
        bigsr = []
        singlei = income[0]
        spousei = income[1]
        joint = singlei + spousei
        for i, seq in zip([singlei, spousei, joint], range(3)):
            mpf = int(i * 0.05)
            if i < 85200:
                mpf = 0
            elif mpf > 18000 and seq + 1 != 3:
                mpf = 18000
            elif mpf > 36000 and seq + 1 == 3:
                mpf = 36000
            ni = i - mpf
            if seq + 1 == 3:
                nci = ni - (132000 * 2)
            else:
                nci = ni - 132000
            if nci < 0:
                nci = 0
            # progressive rate
            if nci <= 50000:
                pr1 = nci * 0.02
            elif nci <= 100000:
                pr1 = 50000 * 0.02 + (nci - 50000) * 0.06
            elif nci <= 150000:
                pr1 = 50000 * 0.02 + 50000 * 0.06 + (nci - 100000) * 0.1
            elif nci <= 200000:
                pr1 = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + (nci - 150000) * 0.14
            elif nci > 200000:
                pr1 = 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.1 + 50000 * 0.14 + (nci - 200000) * 0.17
            # standard rate
            sr1 = ni * 0.15
            if seq == 0:
                pr = [singlei, mpf, pr1]
                sr = [singlei, mpf, sr1]
            elif seq == 1:
                pr = [spousei, mpf, pr1]
                sr = [spousei, mpf, sr1]
            else:
                pr = [joint, mpf, pr1]
                sr = [joint, mpf, sr1]
            bigpr.append(pr)
            bigsr.append(sr)
            # income, income, mpf, mpf, tax
        pr = ["pr", bigpr[0][0], bigpr[0][1], bigpr[1][0], bigpr[1][1], int(bigpr[0][2]+bigpr[1][2])]
        sr = ["sr", bigsr[0][0], bigsr[0][1], bigsr[1][0], bigsr[1][1], int(bigsr[0][2]+bigsr[1][2])]
        jpr = ["jpr", bigpr[2][0], bigpr[2][1], int(bigpr[2][2])]
        jsr = ["jsr", bigsr[2][0], bigsr[2][1], int(bigsr[2][2])]
        a = [pr, sr, jpr, jsr]
        a.sort(key=lambda x: x[-1])
        return a[0]

if __name__ == "__main__":
    interface()