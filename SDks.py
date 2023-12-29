# import user


def data_plans(num):
    if num == 1:
        print('''
        Buy Data Plans
        1.Daily 
        2.Weekly
        3.Monthly
        4.2.-3Month
        5.Always ON
        6.Broadband
        7.Family packs
        8.Hot Deals
        9.Free Youtube
        Deals
        10.Manage Data
        0.Back
        ''')
    if num == 0:
        print('''
             1.Data plans
             2.Get 700MB + 3
             voice mins for N500
             3.Social Bundles
             4.Chat with Zigi
             5. Get 1.5GB for
             N300
            ''')

def data_plans_1(num):
    if num == 1:
        print('''
        1.N50 for 40MB
        2.N100 for 100MB
        3.100 for 
        350MB(IG/TT/YT)
        4.N200 for 200MB
        5.N350 for 1GB
        6.N800 for 3GB
        7.N500 for 2GB
        8.N600 for 2.5GB
        99.Next 
        0.Back
        ''')
        res1 = int(input())
        if res1 == 0:
            data_plans_1(1)
        if res1 == 1:
            data_view(50, "40MB", 'Daily')
        if res1 == 3:
            data_view(300, "350MB", '(IG/TT/YT)')
        if res1 == 2:
            data_view(100, "100MB", 'Daily')
        if res1 == 4:
            data_view(200, "200MB", 'Daily')
        if res1 == 5:
            data_view(350, '1GB', 'Daily')
        if res1 == 6:
            data_view(800, "3GB", '2-day')
        if res1 == 7:
            data_view(500, '2GB', '2-day')
        if res1 == 8:
            data_view(600, '2.5GB', '4-day')

def data_view(amount, data, plan):
    print(f'''
    You will be charged 
    N{amount} for the 
    purchase of {data}
    {plan} Plan. To
    proceed, select: 
    1.Auto-renew
    2.One off
    3.Buy for a Friend
    4.Reedeem Promo
    Code
    0.Back
    ''')
    res = int(input())
    if res == 1 | 2 | 3 | 4:
        print('''
        oops the code
        you dailed is 
        incorrect, please
        try again later 😀
        ''')

    if res == 0:
        data_plans_1(1)



def socials():
    print('''
    1.Whatsapp
    2.2Go
    3.Facebook
    4.Instagram
    5.WeChat
    6.Snapchat
    7.Tiktok
    0.Back
    ''')
    res = int(input())
    if res == 1:
        print('''
        Whatsapp
        1.  Daily N25 for 25 MB
        2. Weekly @ N50 for
        50MB
        3. Monthly @ N150 
        for 150MB
        0.Back
        ''')
        res1 = int(input())
        if res1 == 1:
            data_view(25, "25MB", "Whatsapp Daily")
        if res1 == 2:
            data_view(50, "50MB", 'Whatsapp Weekly')
        if res1 == 3:
            data_view(150, "150MB", 'Whatsapp Monthly')

    if res == 2:
        print('''
                2GO
                1.  Daily N25 for 25 MB
                2. Weekly @ N50 for
                50MB
                3. Monthly @ N150 
                for 150MB
                0.Back
                ''')
        res1 = int(input())
        if res1 == 1:
            data_view(25, "25MB", "2Go Daily")
        if res1 == 2:
            data_view(50, "50MB", '2Go Weekly')
        if res1 == 3:
            data_view(150, "150MB", '2Go Monthly')

    if res == 3:
        print('''
                Facebook
                1.  Daily N25 for 25 MB
                2. Weekly @ N50 for
                50MB
                3. Monthly @ N150 
                for 150MB
                0.Back
                ''')
        res1 = int(input())
        if res1 == 1:
            data_view(25, "25MB", "Facebook Daily")
        if res1 == 2:
            data_view(50, "50MB", 'Facebook Weekly')
        if res1 == 3:
            data_view(150, "150MB", 'Facebook Monthly')

    if res == 4:
        print('''
                Instagram
                1.  Daily N50 for 50 MB
                2. Weekly @ N150 for
                150MB
                3. Monthly @ N250 
                for 250MB
                0.Back
                ''')
        res1 = int(input())
        if res1 == 1:
            data_view(50, "50MB", "Instagram Daily")
        if res1 == 2:
            data_view(150, "150MB", 'Instagram Weekly')
        if res1 == 3:
            data_view(250, "250MB", 'Instagram Monthly')

    if res == 5:
        print('''
                WeChat
                1.  Daily N50 for 50 MB
                2. Weekly @ N100 for
                100MB
                3. Monthly @ N200 
                for 200MB
                0.Back
                ''')
        res1 = int(input())
        if res1 == 1:
            data_view(50, "50MB", "weChat Daily")
        if res1 == 2:
            data_view(100, "100MB", 'weChat Weekly')
        if res1 == 3:
            data_view(200, "200MB", 'weChat Monthly')

    if res == 6:
        print('''
                Snapchat
                1.  Daily N100 for 100 MB
                2. Weekly @ N150 for
                150MB
                3. Monthly @ N200 
                for 200MB
                0.Back
                ''')
        res1 = int(input())
        if res1 == 1:
            data_view(100, "100MB", "Snapchat Daily")
        if res1 == 2:
            data_view(150, "150MB", 'Snapchat Weekly')
        if res1 == 3:
            data_view(200, "200MB", 'Snapchat Monthly')

    if res == 7:
        print('''
                Tiktok
                1.  Daily N50 for 50 MB
                2. Weekly @ N100 for
                100MB
                3. Monthly @ N200 
                for 2000MB
                0.Back
                ''')
        res1 = int(input())
        if res1 == 1:
            data_view(50, "50MB", "Tiktok Daily")
        if res1 == 2:
            data_view(100, "100MB", 'Tiktok Weekly')
        if res1 == 3:
            data_view(200, "200MB", 'Tiktok Monthly')

    if res == 0:
        print('''
            1.Whatsapp
            2.2Go
            3.Facebook
            4.Instagram
            5.WeChat
            6.Snapchat
            7.Tiktok
            0.Back
            ''')