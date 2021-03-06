# Board's cells representation
EC = 0
VC = 8
BC = 9

# List of boards to display
boardsULM = list(range(20))

initBoards =( # 0
             [[EC, EC, BC, BC, EC, EC],
              [EC, EC, EC, EC, EC, BC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 1
             [[BC, BC, BC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 2
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, BC],
              [EC, EC, EC, EC, EC, EC],
              [EC, BC, BC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 3
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC],
              [VC, BC, EC, EC, EC, EC]],
            # 4
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, BC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, EC, EC],
              [VC, EC, EC, BC, EC, EC]],              
            # 5
             [[EC, EC, EC, EC, BC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 6
             [[EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC],
              [EC, EC, EC, BC, BC, EC],
              [VC, EC, EC, EC, EC, EC]],
            # 7
             [[EC, EC, EC, EC, EC, EC, BC, EC],
              [EC, EC, EC, EC, EC, EC, BC, EC],
              [BC, EC, EC, EC, EC, EC, EC, EC],
              [BC, EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC, EC]],
            # 8
             [[EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, BC, BC]],
            # 9
             [[BC, BC, BC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [VC, BC, EC, EC, EC, EC, EC, EC]],
            # 10
             [[BC, BC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, BC, BC]],
            # 11
             [[EC, EC, EC, EC, EC, EC, BC, EC],
              [EC, EC, EC, EC, EC, EC, BC, EC],
              [EC, EC, EC, EC, BC, EC, EC, EC],
              [EC, EC, EC, EC, BC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC, EC]],
            # 12
             [[EC, EC, BC, EC, EC, EC, EC, EC],
              [EC, EC, BC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, BC, EC, EC, EC],
              [EC, EC, EC, EC, BC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC, EC]],
            # 13
             [[EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, BC, BC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, BC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC, EC]],
            # 14
             [[EC, EC, BC, BC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC, EC]],
            # 15
             [[EC, EC, EC, BC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC]],
            # 16
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, BC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, EC, EC, EC],
              [VC, BC, EC, EC, EC, EC, EC]],
            # 17
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [BC, BC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [BC, BC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC]],
            # 18
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [BC, EC, EC, EC, EC, EC, EC],
              [BC, EC, BC, EC, EC, EC, EC],
              [EC, EC, BC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC]],
            # 19
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, BC, EC],
              [EC, EC, EC, BC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, BC, BC]],
            # 20
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, BC, BC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC]],
            # 21
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, BC, EC, EC, BC],
              [EC, EC, EC, BC, EC, EC, BC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC]],
            # 22
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, BC, BC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, BC],
              [VC, EC, EC, EC, EC, EC, BC]],
            # 23
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, BC, EC, EC, EC, EC, BC],
              [EC, BC, EC, EC, EC, EC, BC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, EC, EC, EC, EC, EC, EC]],
            # 24
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, BC, EC, EC],
              [EC, EC, BC, EC, BC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, BC, EC, EC, EC, EC, EC]],
            # 25
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, BC, EC, EC, BC, EC],
              [EC, EC, BC, EC, EC, BC, EC],
              [VC, EC, EC, EC, EC, EC, EC]],
            # 26
             [[EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, BC],
              [EC, EC, EC, EC, BC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [EC, EC, EC, EC, EC, EC, EC],
              [VC, BC, BC, EC, EC, EC, EC]],
)