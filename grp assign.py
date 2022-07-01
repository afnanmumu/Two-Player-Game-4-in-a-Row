function ALPHA-BETA-SEARCH(state, depth)
    v <- MAX-VALUE(state, depth, -Inf, +Inf)
    return the move which results in value v
function MAX-VALUE(state, alpha, beta, depth) returns a utility
    value if state is terminal return Utility(state) if
    depth == 0 return Evaluate(state)
    v = -Inf
for each possible action a possible from state do
    v = Max(v, MIN-VALUE(RESULTS(state,a),alpha, beta,
    depth-1))
    if v >= beta return v
    alpha = MAX(alpha, v)
    return v

function MIN-VALUE(state, alpha, beta, depth) returns a utility
    value if state is terminal return Utility(state) if
    depth == 0 return Evaluate(state)
    v = +Inf
    for each possible action a possible from state do
    v = MIN(v, MAX-VALUE(RESULTS(state,a),alpha, beta,
    depth-1))
    if v <= alpha return v
    beta = MIN(beta, v)
    return v