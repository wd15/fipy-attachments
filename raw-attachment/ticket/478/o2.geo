Point(1) = {0, 0, 0, 1.0};
Point(2) = {1, 0, 0, 1.0};
Point(3) = {-1, 0, 0, 1.0};
Point(4) = {1.5, 0, 0, 1.0};
Point(5) = {-1.5, 0, 0, 1.0};
Point(6) = {0, 1.5, 0, 1.0};
Point(7) = {0, -1.5, 0, 1.0};
Point(8) = {0, -1, 0, 1.0};
Point(9) = {0, 1, 0, 1.0};
Circle(1) = {3, 1, 9};
Circle(2) = {9, 1, 2};
Circle(3) = {2, 1, 8};
Circle(4) = {8, 1, 3};
Circle(5) = {5, 1, 6};
Circle(6) = {6, 1, 4};
Circle(7) = {4, 1, 7};
Circle(8) = {7, 1, 5};
Line Loop(9) = {1, 2, 3, 4};
Line Loop(10) = {5, 6, 7, 8};
Plane Surface(11) = {9, 10};
Plane Surface(12) = {9};
Delete {
  Surface{12, 11};
}
Plane Surface(11) = {10};
