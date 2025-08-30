def join_or(lst, symbol=', ', final='or'):
    final_string = ''
    if lst:
        if len(lst) == 1:
            print(lst[0])
        elif len(lst) == 2:
            print(f'{lst[0]} {final} {lst[1]}')
        else:
            for indx in range(len(lst)):
                if indx < (len(lst) - 1):
                    final_string += f'{lst[indx]}{symbol}'
                else:
                    final_string += f'{final} {lst[indx]}'
            print(final_string)
    
join_or([1, 2])                   # => "1 or 2"
join_or([1, 2, 3])                # => "1, 2, or 3"
join_or([1, 2, 3], '; ')          # => "1; 2; or 3"
join_or([1, 2, 3], ', ', 'and')   # => "1, 2, and 3"