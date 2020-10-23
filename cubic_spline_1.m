function cubic_spline_1()
%CUBIC_SPLINE Summary of this function goes here
%   Detailed explanation goes here
    k = 4;
    
    x = [0 1 2 3 4 5];
    y = [0 -1 1 0 2 -1];
    
    sp = csapi( x, y );
    transpose(sp.coefs)

end
