function res = progonka()
    A = [391 -1 0 0 0 0 0 0 0 0; -4 72 -27 0 0 0 0 0 0 0; 0 7 -19 7 0 0 0 0 0 0; 0 0 -134 -460 30 0 0 0 0 0; 0 0 0 -23 281 -83 0 0 0 0;
    0 0 0 0 -374 896 -353 0 0 0; 0 0 0 0 0 -238 -716 86 0 0; 0 0 0 0 0 0 -66 147 63 0; 0 0 0 0 0 0 0 109 458 -200; 0 0 0 0 0 0 0 0 626 721];
    B = [969; 718; 571; 27; -645; -203; -733; -939; 879; -398];
    [a, b] = size(A);
    b = get_b_array(A);
    c = get_c_array(A);
    d = get_d_array(A);
    tau = 0;
    sigma = 0;
    sigmas = zeros(1, a - 1);
    lamda = 0;
    lamdas = zeros(1, a);
    i = 1;
    while i <= a
        if i == 1
            tau = get_tau(0, 0, c(i));
        else
  
            tau = get_tau(b(i - 1), sigma, c(i));
        end
        
        if i ~= a 
            sigma = get_sigma(d(i), tau);
            sigmas(i) = sigma;
        end
        
        if i == 1
            lamda = get_lamda(B(i), 0, 0, tau);
        else
            lamda = get_lamda(B(i), b(i - 1), lamda, tau);
        end
        lamdas(i) = lamda;
        i = i + 1;
    end
    answers = zeros(1, a);
    i = a;
    while i > 0
        if i == a
            x = lamdas(i);
        else
            x = sigmas(i)*answers(i+1) + lamdas(i);
        end
        answers(i) = x;
        i = i - 1;
    end
    
    res = answers;
end

function res = get_d_array(matrix)
    [a b] = size(matrix);    
    res = zeros(1, a - 1);
    i = 1;
    while i < a
        res(i) = matrix(i, i + 1);
        i = i +1;
    end
end

function res = get_c_array(matrix)
    [a b] = size(matrix);    
    res = zeros(1, a);
    i = 1;
    while i <= a
        res(i) = matrix(i, i);
        i = i + 1;
    end
end

function res = get_b_array(matrix)
    [a b] = size(matrix);    
    res = zeros(1, a - 1);
    i = 1;
    while i < a
        res(i) = matrix(i + 1, i);
        i = i +1;
    end
end

function res = get_tau(b, sigma, c)
    res = b*sigma + c;
end

function res = get_sigma(d, tau)
    res = -d/tau;
end

function res = get_lamda(r, b, lamda, tau)
    res = (r - lamda*b)/tau;
end