class Cards:
    def __init__(self):
        self.jack=11
        self.queen=12
        self.king=13
        self.ace=14
        self.diamond=1000
        self.sapde=2000
        self.club=4000
        self.heart=3000

        self.dict_diamond={2:self.diamond,3:self.diamond,4:self.diamond,5:self.diamond,6:self.diamond,7:self.diamond,8:self.diamond,9:self.diamond,10:self.diamond,self.jack:self.diamond
            ,self.queen:self.diamond,self.king:self.diamond,self.ace:self.diamond}

        self.dict_sapde={2:self.sapde,3:self.sapde,4:self.sapde,5:self.sapde,6:self.sapde,7:self.sapde,8:self.sapde,
                9:self.sapde,10:self.sapde,self.jack:self.sapde,self.queen:self.sapde,self.king:self.sapde,self.ace:self.sapde}

        self.dict_club={2:self.club,3:self.club,4:self.club,5:self.club,6:self.club,7:self.club,8:self.club,9:self.club,10:self.club,
                        self.jack:self.club,self.queen:self.club,self.king:self.club,self.ace:self.club}

        self.dict_heart={2:self.heart,3:self.heart,4:self.heart,5:self.heart,6:self.heart,7:self.heart,8:self.heart,
                         9:self.heart,10:self.heart,self.jack:self.heart,self.queen:self.heart,self.king:self.heart,self.ace:self.heart}
