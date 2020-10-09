function cubic_spline_2()
    x = [-1 0.5 2];
    y = [0 2 -1];
    min = -1;
    max = 2;
    
    Llist = zeros(1,length(x)-1);
    for i=1:length(x)-1
        Llist(i) = x(i+1)-x(i);
    end
    
    unknowns = 3*length(Llist);
    Ln = Llist(length(Llist));
    B = [0 0 0; 0 0 -1; 0 -2 0];
    T = [0 0 0; 0 1 0; 0 0 0];
    V = [Ln^3 Ln^2 Ln; 0 0 0; 6*Ln 2 0];
    Alist = zeros(3,unknowns,length(Llist));
    
    for L = 1:length(Llist)
        if L == 1
            Alist(:,:,L) = [calc_A(Llist(L)) B zeros(3,unknowns-L*6)];
            M = Alist(:,:,L);
        elseif L == length(Llist)
            Alist(:,:,L) = [T zeros(3,unknowns-6) V];
            M = [M;Alist(:,:,L)];
        else
            Alist(:,:,L) = [zeros(3,(L-1)*3) calc_A(Llist(L)) B zeros(3,unknowns-(L+1)*3)];
            M = [M;Alist(:,:,L)];
        end
        
    end
    
    b = zeros(unknowns,1);
    for j = 1:unknowns
        if mod(j,3) == 0
            b(j-2) = y(j/3+1)-y((j/3));
        end
    end
    c = M\b    
    
end

function A = calc_A(L)
    A = [L^3 L^2 L; 3*L^2 2*L 1; 6*L 2 0];
end
