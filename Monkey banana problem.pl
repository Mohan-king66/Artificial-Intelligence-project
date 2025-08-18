% Monkey and Banana Problem in Prolog
% State Representation: state(MonkeyLocation, MonkeyOnBox, BoxLocation, HasBanana)

% Initial state: monkey at door, box at window, not on box, doesn't have banana
% Goal state: monkey has banana

% Possible moves:

% 1. Monkey walks from one place to another
move(state(Place1, on_floor, Place1, has_not),
     walk(Place1, Place2),
     state(Place2, on_floor, Place1, has_not)).

% 2. Monkey pushes the box from one place to another (must be on floor and at same place as box)
move(state(Place, on_floor, Place, has_not),
     push(Place, Place2),
     state(Place2, on_floor, Place2, has_not)).

% 3. Monkey climbs onto the box (must be at same place as box)
move(state(Place, on_floor, Place, has_not),
     climb,
     state(Place, on_box, Place, has_not)).

% 4. Monkey climbs down from box
move(state(Place, on_box, Place, has_not),
     climb_down,
     state(Place, on_floor, Place, has_not)).

% 5. Monkey grasps banana (must be on box and at banana's location)
move(state(middle, on_box, middle, has_not),
     grasp,
     state(middle, on_box, middle, has)).

% Recursive solution finder
can_get(state(_, _, _, has), []).  % If monkey already has banana, done.

can_get(State1, [Move | RestMoves]) :-
    move(State1, Move, State2),
    can_get(State2, RestMoves).

% Initial State
start(state(door, on_floor, window, has_not)).
