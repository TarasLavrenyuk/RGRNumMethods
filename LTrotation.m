function res = LTrotation()
    A = [-26 -81 84 -13 77 15 -96 54 65; -45 81 46 -62 -39 -33 38 80 -64; 49 17 68 95 -36 29 -70 93 -90; 63 68 2 -45 46 62 21 2 97; -14 76 26 67 -18 16 7 -32 26;
        -64 -68 -45 -64 -39 7 -54 58 27; 18 68 81 -25 73 27 59 -39 -97; -53 16 -33 -11 -88 53 99 -39 81; -66 24 60 -7 -97 -32 40 -11 -50]; 
    b = [33; -62; -41; -84; 5; -41; -8; 52; 34];
    [a, k] = size(A);
    N = a;
    T_array_size = 0;
    T_array = zeros(9, 9, T_array_size);
    current_A = A;
    
    i = 1;
    while i < N
        j = i + 1;
        while j <= N
            Cij = get_Cij(current_A, i, j);
            Sij = get_Sij(current_A, i, j);
            T = get_single_matrix(N);
            T(i, i) = Cij;
            T(j, j) = Cij;
            T(i, j) = -Sij;
            T(j, i) = Sij;
%             disp(T);
            T_array(:, :, T_array_size + 1) = T;
            T_array_size = T_array_size + 1;
            current_A = current_A*T;
%             disp(current_A);
            j = j + 1;
        end
        i = i + 1;
    end
    L = current_A;
    Y_array = get_y_array(L, b, N);
    disp(Y_array);
    
    Tt = get_T_transponovana(T_array);
    res = Tt*transpose(Y_array);
end


function c = get_Cij(matrix, i, j)
    c = matrix(i, i)/(sqrt(matrix(i, i)*matrix(i, i) + matrix(i, j)*matrix(i, j)));
end

function s = get_Sij(matrix, i, j)
    s = matrix(i, j)/(sqrt(matrix(i, i)*matrix(i, i) + matrix(i, j)*matrix(i, j)));
end

function SingleMatrix = get_single_matrix(N)
    SingleMatrix = eye(N);
end

function y = get_y_array(L, b, N)
    y = zeros(1, N);
    k = 1;
    while k <= 9
        suma = 0;
        j = 1;
        if k-1 >= j
            while j <= k - 1
                suma = suma + L(k, j) * y(j);
                j = j + 1;
            end
        end
        y(k) = (b(k) - suma) / L(k, k);
        k = k + 1;
    end
end

function res = get_T_transponovana(T_array)
    res = T_array(:,:,1);
    i = 2;
    while i <= 36
        res = res * T_array(:,:,i);
        i = i + 1;
    end
end




















