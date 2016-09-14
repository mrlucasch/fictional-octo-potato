// tests.cpp
#include "squareRoot.cpp"
#include <gtest/gtest.h>
 
TEST(SquareRootTest, PositiveNos) { 
    RecordProperty("Points",8);
    ASSERT_EQ(6, squareRoot(36.0));
    ASSERT_EQ(18.0, squareRoot(324.0));
    ASSERT_EQ(25.4, squareRoot(645.16));
    ASSERT_EQ(0, squareRoot(0.0));
}
 
TEST(SquareRootTest2, NegativeNos) {
    RecordProperty("Points",4);
    ASSERT_EQ(-1.0, squareRoot(-15.0));
    ASSERT_EQ(-1.0, squareRoot(-0.2));
}



TEST(AdditionTest1, OneZeroNum) {

    RecordProperty("Points",2);
    ASSERT_EQ(1.0, addition(1,0));
    ASSERT_EQ(150, addition(0,150));
}

TEST(AdditionTest2, PositiveNumbers) {

    RecordProperty("Points",2);
    ASSERT_EQ(1015, addition(15,1000));
    ASSERT_EQ(60, addition(10,50));
}

TEST(AdditionTest3, ZeroNumbers) {

    RecordProperty("Points",1);
    ASSERT_EQ(0, addition(0,0));
}

TEST(AdditionTest4, Wrong) {

    RecordProperty("Points",2);
    ASSERT_EQ(155, addition(5,150));
    ASSERT_EQ(100, addition(25,75));
}

TEST(AdditionTest5, OneWrong) {

    RecordProperty("Points",4);
    ASSERT_EQ(160, addition(10,150));
    ASSERT_EQ(100, addition(25,75));
}



TEST(AdditionTest6, NegativeNumbers) {

    RecordProperty("Points",4);
    ASSERT_EQ(0, addition(-10,10));
    ASSERT_EQ(60, addition(70,-10));
    ASSERT_EQ(-50, addition(-20,-30));
    ASSERT_EQ(120, addition(130,-10));
}


TEST(StringTest1, Correct) {

    RecordProperty("Points",2);
    ASSERT_EQ("olleh", reverse("hello"));
}

TEST(StringTest2, Incorrect) {

    RecordProperty("Points",2);
    ASSERT_EQ("ollhe", reverse("hello"));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
