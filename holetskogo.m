function res = holetskogo()
    A = [241 -49 -64 -32 83 -73 57 66 -17 -47 -1; -49 42 65 -9 -45 25 8 10 0 16 -54; -64 65 207 71 -195 103 41 27 43 92 -167;
        -32 -9 71 241 -129 79 83 144 98 30 -50; 83 -45 -195 -129 216 -93 -48 -36 -86 -84 83; -73 25 103 79 -93 218 -36 -2 -58 182 -213;
        57 8 41 83 -48 -36 236 62 152 -69 227; 66 10 27 144 -36 -2 62 245 44 -35 -113; -17 0 43 98 -86 -58 152 44 241 -25 -250;
        -47 16 92 30 -84 182 -69 -35 -25 244 210];
    tic
    [matrix_len, b] = size(A);
    u = zeros(matrix_len, matrix_len);
    i = 1;
    while i <= matrix_len
        j = i;
        while j <= matrix_len
            if i == j
                sum = 0;
                ii = 1;
                while ii <= i
                    sum = sum + u(ii, i) * u(ii, i);
                    ii = ii + 1;
                end
                u(i, j) = sqrt(A(i, j) - sum);
            else
                sum = 0;
                k = 1;
                while k <= i
                    sum = sum + u(k, i) * u(k, j);
                    k = k + 1;
                end
                u(i, j) = (A(i, j) - sum) / u(i, i);
            end
            j = j + 1;
        end
        i = i + 1;
    end
    
    
    transponed = transpone(u);    
    determinator = determinant(u);
    obernenaQuad = obernenaA(u);

    transponed = [transponed A(:,b)];
    
    
    result = solve_down_triangle(transponed);
    
    
    
    u = [u transpose(result)];
    
    
    
    result = solve_upper_triangle(u);
    
    disp(transpose(result))
    
%     disp('Determinator')
%     disp(determinator)
%     disp('Obernena')
%     disp(obernenaQuad)
    res = result;
    toc
end



function res = transpone(m)
    [matrix_len, b] = size(m);
    u = zeros(matrix_len, matrix_len);
    
    i = 1;
    while i <= matrix_len
        j = 1;
        while j <= matrix_len
            u(i, j) = m(j, i);
            j = j + 1;
        end
        i = i + 1;
    end
    res = u;
end

function res = determinant(matr)
    mult = matr(1, 1);
    [matr_length, j] = size(matr);
    i = 2;
    while i <= matr_length
        mult = mult * matr(i, i);
        i = i + 1;
    end
    res = mult * mult;
end

function res = obernenaA(u)
    [matr_length, j] = size(u);
%     t = zeros(matr_length, matr_length);
    aober = zeros(matr_length, matr_length);
        
    r = 1;
    while r <= matr_length
        s = r;
        while s <= matr_length
            sum = 0;
            k = s;
            while k <= matr_length
                sum = sum + Ti(r, k, u) * Ti(s, k, u);
                k = k + 1;
            end
            aober(r, s) = sum;
            s = s + 1;
        end
        r = r + 1;
    end
    res = aober;
end

function res = Ti(i, j, u)
    
    if i == j
        res =  1 / u(i, i);
    else
        sum = 0;
        k = i + 1;
        while k <= j
            sum = sum + u(i, k) * Ti(k, j, u); 
            k = k + 1;
        end
        res =  -1 * sum / u(i, j);
    end
        
end

function res = solve_down_triangle(m)
    [matrix_length, b] = size(m);
    y = zeros(1, matrix_length);
    i = 1;
    while i <= matrix_length
        sum = 0;
        j = 1;
        while j <= i
            sum = sum + m(i, j) * y(j);
            j = j + 1;
        end
        y(i) = (m(i, b) - sum) / m(i, i);
        i = i + 1;
    end
    res = y;
end

function res = solve_upper_triangle(m)
    [matrix_length, b] = size(m);
    x = zeros(1, matrix_length);
    
    k = matrix_length;
    while k >= 1
        sum = 0;
        j = k + 1;
        while j <= matrix_length
            sum = sum + m(k, j) * x(j);
            j = j + 1;
        end
        x(k) = (m(k, b) - sum) / m(k, k);
        k = k - 1;
    end
    res = x;
end






























