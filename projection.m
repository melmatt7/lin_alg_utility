function [P] = projection(A,B)
%PROJECTION Summary of this function goes here
%   Detailed explanation goes here
    dot(A,B)
    norm(B)^2
    P = (dot(A,B)/norm(B)^2)*B;

end

