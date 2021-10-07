def solution(ps, location):
    ls = list(range(len(ps)))
    result = {}
    order = 1
    while ps:
        m_index = ps.index(max(ps))
        ps = ps[m_index: ] + ps[:m_index]
        ls = ls[m_index: ] + ls[:m_index]
        ps.pop(0)
        result[ls.pop(0)] = order
        order += 1
    return result[location]
        
    
