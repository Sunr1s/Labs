
X  = [ 350   630   996  1121  1251  1663  1998  2386];
Y  = [18  21  15   7   8  15  17  14];
XW  = [1803   583  1045  1058];

dX = (X(end)-X(1))/100;
XW100 = X(1) : dX : X(end);
YW = interp1(X,Y,XW100, 'nearest');
YW2_2 = interp1(X,Y,XW100, 'linear');

plot(XW100, YW, 'b');
hold("on");

y1 = interp1(X,Y,XW,'nearest');
plot(XW,y1, 'bo');
plot(XW100, YW2_2, 'g');

y2 = interp1(X,Y,XW,'linear');
plot(XW,y2, 'go');

c = spline(X,Y,XW100);
plot(XW100, c, 'r');
y3 = interp1(X,Y,XW,'spline');
plot(XW, y3, 'ro');
legend('nearest','nearest control points','linear','linear control points','spline','spline control points');
hold("off");
SumY1 = sum(y1);
display("Sum of honey by nearest method: "+ SumY1);
SumY2 = sum(y2);
display("Sum of honey by linear method: "+ SumY2);
SumY3 = sum(y3);
display("Sum of honey by spline method: "+ SumY3);