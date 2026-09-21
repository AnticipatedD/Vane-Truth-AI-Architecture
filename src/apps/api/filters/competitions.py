def filter_competitions(queryset, params):
    if 'search' in params:
        return queryset.filter(title__icontains=params['search'])
    return queryset
