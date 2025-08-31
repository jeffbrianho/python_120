def join_or(lst, symbol=', ', final='or'):
    final_string = ''
    if lst:
        if len(lst) == 1:
            return lst[0]
        elif len(lst) == 2:
            return f'{lst[0]} {final} {lst[1]}'
        else:
            for indx in range(len(lst)):
                if indx < (len(lst) - 1):
                    final_string += f'{lst[indx]}{symbol}'
                else:
                    final_string += f'{final} {lst[indx]}'
            return final_string
    
join_or([1, 2])                   # => "1 or 2"
join_or([1, 2, 3])                # => "1, 2, or 3"
join_or([1, 2, 3], '; ')          # => "1; 2; or 3"
join_or([1, 2, 3], ', ', 'and')   # => "1, 2, and 3"


"""
go through each winning possibliity if 2/3 are met take the and the number is available. take that square


"""