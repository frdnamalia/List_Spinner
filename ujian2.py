print("="*50)
print("---List Spinner---\n")
print("by Fardhina Amalia")

print("="*50)
print("===SEBELUM===")
Matrix1=[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]
print(Matrix1)

# [[4, 8, 12, 16] [0][3] [1][3] [2][3] [3][3]
# [3, 7, 11, 15], [0][2] [1][2] [2][2] [3][2]
# [2, 6, 10, 14],
# [1, 5, 9, 13]]

def Mat(x):
    Mat1=[]
    for j in range(len(x)-1,-1,-1): #0,1,2,3,4
        cangkang=[]
        for i in range(len(x)): # 4,3,2,1,0
            cangkang.append(x[i][j])
        Mat1.append(cangkang)
    return Mat1
Mat2=Mat(Matrix1)
print("===SESUDAH===")
print(Mat2)