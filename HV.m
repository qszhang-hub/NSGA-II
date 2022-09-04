%------------------------------- Reference --------------------------------
% E. Zitzler and L. Thiele, Multiobjective evolutionary algorithms: A
% comparative case study and the strength Pareto approach, IEEE
% Transactions on Evolutionary Computation, 1999, 3(4): 257-271.
%--------------------------------------------------------------------------
% This function can be used to calculate HyperVolume for multi- and
% many-optimization problems, where
% F: non-dominated set of objective values
% NP: problem number
% HV_Score: HyperVolume value for given F.
% Created by:
% Name: Abhishek Kumar
% email id: abhishek.kumar.eee13@iitbhu.ac.in 
%--------------------------------------------------------------------------
function HV_Score = HV(F,NP)
    %% Normalization of objective functions
    [N,M]  = size(F); % N is population size and M is number of objectives
    if N > max(100,30*M)
        warning('Population size is higher than predefined limit');
        F = F(randperm(N,max(100,30*M)),:);
        N = max(100,30*M);
    end
    fmin   = min(min(F,[],1),zeros(1,M));
    fmax   = load(['RefPoints\nadir_' num2str(NP) '.txt']);
    F = (F-repmat(fmin,N,1))./repmat((fmax-fmin)*1.1,N,1);
    F(any(F>1,2),:) = [];
    RefPoint = ones(1,M); % The reference point is set to (1,1,...)
    %% Calculation of HV value
    if isempty(F)
        HV_Score = 0;
    elseif M < 4 
        %% Calculate the exact HV value
        pl = sortrows(F);
        S  = {1,pl};
        for k = 1 : M-1
            S_ = {};
            for i = 1 : size(S,1)
                Stemp = Cut(cell2mat(S(i,2)),k,RefPoint);
                for j = 1 : size(Stemp,1)
                    temp(1) = {cell2mat(Stemp(j,1))*cell2mat(S(i,1))};
                    temp(2) = Stemp(j,2);
                    S_      = Add(temp,S_);
                end
            end
            S = S_;
        end
        HV_Score = 0;
        for i = 1 : size(S,1)
            p     = Head(cell2mat(S(i,2)));
            HV_Score = HV_Score + cell2mat(S(i,1))*abs(p(M)-RefPoint(M));
        end
    else 
        %% Calculation of the HV value by Monte Carlo estimation 
        SampleNum = 1000000;
        MaxValue  = RefPoint;
        MinValue  = min(F,[],1);
        Samples   = unifrnd(repmat(MinValue,SampleNum,1),repmat(MaxValue,SampleNum,1));
        %% find the non-dominated samples wrt F
        for i = 1 : size(F,1)
            domi = true(size(Samples,1),1);
            m    = 1;
            while m <= M && any(domi)
                domi = domi & F(i,m) <= Samples(:,m);
                m    = m + 1;
            end
            Samples(domi,:) = [];
        end
        %% estimate of HV value
        HV_Score = prod(MaxValue-MinValue)*(1-size(Samples,1)/SampleNum);
    end
end

function S = Cut(pl,k,RefPoint)
    p  = Head(pl);
    pl = Tail(pl);
    ql = [];
    S  = {};
    while ~isempty(pl)
        ql  = Insert(p,k+1,ql);
        p_  = Head(pl);
        cell_(1,1) = {abs(p(k)-p_(k))};
        cell_(1,2) = {ql};
        S   = Add(cell_,S);
        p   = p_;
        pl  = Tail(pl);
    end
    ql = Insert(p,k+1,ql);
    cell_(1,1) = {abs(p(k)-RefPoint(k))};
    cell_(1,2) = {ql};
    S  = Add(cell_,S);
end

function ql = Insert(p,k,pl)
    flag1 = 0;
    flag2 = 0;
    ql    = [];
    hp    = Head(pl);
    while ~isempty(pl) && hp(k) < p(k)
        ql = [ql;hp];
        pl = Tail(pl);
        hp = Head(pl);
    end
    ql = [ql;p];
    m  = length(p);
    while ~isempty(pl)
        q = Head(pl);
        for i = k : m
            if p(i) < q(i)
                flag1 = 1;
            else
                if p(i) > q(i)
                    flag2 = 1;
                end
            end
        end
        if ~(flag1 == 1 && flag2 == 0)
            ql = [ql;Head(pl)];
        end
        pl = Tail(pl);
    end  
end

function p = Head(pl)
    if isempty(pl)
        p = [];
    else
        p = pl(1,:);
    end
end

function ql = Tail(pl)
    if size(pl,1) < 2
        ql = [];
    else
        ql = pl(2:end,:);
    end
end

function S_ = Add(cell_,S)
    n = size(S,1);
    m = 0;
    for k = 1 : n
        if isequal(cell_(1,2),S(k,2))
            S(k,1) = {cell2mat(S(k,1))+cell2mat(cell_(1,1))};
            m = 1;
            break;
        end
    end
    if m == 0
        S(n+1,:) = cell_(1,:);
    end
    S_ = S;     
end
