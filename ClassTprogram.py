import math 

class T(object): #creating a Python Class 
    def __init__(self, A, B, C): #defining a method to declare the 3 sets of points
        self.Ax = A[0]
        self.Ay = A[1]
        self.Bx = B[0]
        self.By = B[1]
        self.Cx = C[0]
        self.Cy = C[1]

    def A(self): #Method 1: Calculating the area using the equation below
        return abs(0.5 * ((self.Ax*self.By - self.Ax*self.Cy) + (self.Bx*self.Cy - self.Bx*self.Ay) + (self.Cx*self.Ay - self.Cx*self.By)))

    def Per(self): #Method 2: calculating the perimeter using the distance formula   
        ab = math.sqrt((self.Ax-self.Bx)**2 + (self.Ay - self.By)**2)
        bc = math.sqrt((self.Bx-self.Cx)**2 + (self.By - self.Cy)**2)
        ca = math.sqrt((self.Cx-self.Ax)**2 + (self.Cy - self.Ay)**2)
        return (ab+bc+ca)

    def Center(self): #Method 3: Center of the triangle
        C = float(((self.Ax + self.Bx + self.Cx)/3)) , float((self.Ay + self.By + self.Cy)/3)
        return C
        

    def longest_side(self): #Method 4: Checking for longest side of the triangle
        c = math.sqrt((self.Ax-self.Bx)**2 + (self.Ay - self.By)**2)
        a = math.sqrt((self.Bx-self.Cx)**2 + (self.By - self.Cy)**2)
        b = math.sqrt((self.Cx-self.Ax)**2 + (self.Cy - self.Ay)**2)

        if a > b and c:
            return a
        elif b > a and c:
            return b
        else:
            return c
    def RightT(self): #A final method to decide if the triangle is a right Triangle
        c = math.sqrt((self.Ax-self.Bx)**2 + (self.Ay - self.By)**2)
        a = math.sqrt((self.Bx-self.Cx)**2 + (self.By - self.Cy)**2)
        b = math.sqrt((self.Cx-self.Ax)**2 + (self.Cy - self.Ay)**2)

        angle_a = math.cos(b/a)
        deg_a = math.degrees(angle_a)
        angle_b = math.cos(c/a)
        deg_b = math.degrees(angle_b)
        angle_c = math.cos(b/a)
        deg_c = math.degrees(angle_c)

        if deg_a == 90:
            return "True"
        elif deg_b == 90:
            return "True"
        elif deg_c == 90:
            return "True"
        else:
            return "False"

def main():

    
    X = T((3,-5),(-7,9),(8,-2))#Example set of triangle coordinates
    print("Area is "+str(X.A())) #50
    print("Perimeter is "+str(X.Per()))#41.6366776666
    print("Center is "+str(X.Center()))#(1.333,0.6666)
    print("Longest side is "+str(X.longest_side()))#18.601 #hyp
    print("Is this a right Traingle?"+X.RightT())#False

main()


