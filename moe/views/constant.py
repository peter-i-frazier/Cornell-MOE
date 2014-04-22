# -*- coding: utf-8 -*-
"""Route names and endpoints for all MOE routes."""
from collections import namedtuple

MoeRoute = namedtuple('MoeRoute', ['route_name', 'endpoint'])

GP_EI_ROUTE_NAME = 'gp_ei'
GP_EI_ENDPOINT = '/gp/ei'
GP_EI_MOE_ROUTE = MoeRoute(GP_EI_ROUTE_NAME, GP_EI_ENDPOINT)
GP_EI_PRETTY_ROUTE_NAME = 'gp_ei_pretty'
GP_EI_PRETTY_ENDPOINT = '/gp/ei/pretty'
GP_EI_PRETTY_MOE_ROUTE = MoeRoute(GP_EI_PRETTY_ROUTE_NAME, GP_EI_PRETTY_ENDPOINT)

GP_MEAN_VAR_ROUTE_NAME = 'gp_mean_var'
GP_MEAN_VAR_ENDPOINT = '/gp/mean_var'
GP_MEAN_VAR_MOE_ROUTE = MoeRoute(GP_MEAN_VAR_ROUTE_NAME, GP_MEAN_VAR_ENDPOINT)
GP_MEAN_VAR_PRETTY_ROUTE_NAME = 'gp_mean_var_pretty'
GP_MEAN_VAR_PRETTY_ENDPOINT = '/gp/mean_var/pretty'
GP_MEAN_VAR_PRETTY_MOE_ROUTE = MoeRoute(GP_MEAN_VAR_PRETTY_ROUTE_NAME, GP_MEAN_VAR_PRETTY_ENDPOINT)

GP_NEXT_POINTS_EPI_ROUTE_NAME = 'gp_next_points_epi'
GP_NEXT_POINTS_EPI_ENDPOINT = '/gp/next_points/epi'
GP_NEXT_POINTS_EPI_MOE_ROUTE = MoeRoute(GP_NEXT_POINTS_EPI_ROUTE_NAME, GP_NEXT_POINTS_EPI_ENDPOINT)
GP_NEXT_POINTS_EPI_PRETTY_ROUTE_NAME = 'gp_next_points_epi_pretty'
GP_NEXT_POINTS_EPI_PRETTY_ENDPOINT = '/gp/next_points/epi/pretty'
GP_NEXT_POINTS_EPI_PRETTY_MOE_ROUTE = MoeRoute(GP_NEXT_POINTS_EPI_PRETTY_ROUTE_NAME, GP_NEXT_POINTS_EPI_PRETTY_ENDPOINT)

GP_NEXT_POINTS_KRIGING_ROUTE_NAME = 'gp_next_points_kriging'
GP_NEXT_POINTS_KRIGING_ENDPOINT = '/gp/next_points/kriging'
GP_NEXT_POINTS_KRIGING_MOE_ROUTE = MoeRoute(GP_NEXT_POINTS_KRIGING_ROUTE_NAME, GP_NEXT_POINTS_KRIGING_ENDPOINT)
GP_NEXT_POINTS_KRIGING_PRETTY_ROUTE_NAME = 'gp_next_points_kriging_pretty'
GP_NEXT_POINTS_KRIGING_PRETTY_ENDPOINT = '/gp/next_points/kriging/pretty'
GP_NEXT_POINTS_KRIGING_PRETTY_MOE_ROUTE = MoeRoute(GP_NEXT_POINTS_KRIGING_PRETTY_ROUTE_NAME, GP_NEXT_POINTS_KRIGING_PRETTY_ENDPOINT)

GP_NEXT_POINTS_CONSTANT_LIAR_ROUTE_NAME = 'gp_next_points_constant_liar_route_name'
GP_NEXT_POINTS_CONSTANT_LIAR_ENDPOINT = '/gp/next_points/constant_liar'
GP_NEXT_POINTS_CONSTANT_LIAR_MOE_ROUTE = MoeRoute(GP_NEXT_POINTS_CONSTANT_LIAR_ROUTE_NAME, GP_NEXT_POINTS_CONSTANT_LIAR_ENDPOINT)
GP_NEXT_POINTS_CONSTANT_LIAR_PRETTY_ROUTE_NAME = 'gp_next_points_constant_liar_pretty'
GP_NEXT_POINTS_CONSTANT_LIAR_PRETTY_ENDPOINT = '/gp/next_points/constant_liar/pretty'
GP_NEXT_POINTS_CONSTANT_LIAR_PRETTY_MOE_ROUTE = MoeRoute(GP_NEXT_POINTS_CONSTANT_LIAR_PRETTY_ROUTE_NAME, GP_NEXT_POINTS_CONSTANT_LIAR_PRETTY_ENDPOINT)

ALL_REST_MOE_ROUTES = [
        GP_EI_MOE_ROUTE,
        GP_MEAN_VAR_MOE_ROUTE,
        GP_NEXT_POINTS_EPI_MOE_ROUTE,
        GP_NEXT_POINTS_KRIGING_MOE_ROUTE,
        GP_NEXT_POINTS_CONSTANT_LIAR_MOE_ROUTE,
        ]

ALL_NEXT_POINTS_MOE_ROUTES = [
        GP_NEXT_POINTS_EPI_MOE_ROUTE,
        GP_NEXT_POINTS_KRIGING_MOE_ROUTE,
        GP_NEXT_POINTS_CONSTANT_LIAR_MOE_ROUTE,
        ]

ALL_PRETTY_MOE_ROUTES = [
        GP_EI_PRETTY_MOE_ROUTE,
        GP_MEAN_VAR_PRETTY_MOE_ROUTE,
        GP_NEXT_POINTS_EPI_PRETTY_MOE_ROUTE,
        GP_NEXT_POINTS_KRIGING_PRETTY_MOE_ROUTE,
        GP_NEXT_POINTS_CONSTANT_LIAR_PRETTY_MOE_ROUTE,
        ]

ALL_MOE_ROUTES = []
ALL_MOE_ROUTES.extend(ALL_REST_MOE_ROUTES)
ALL_MOE_ROUTES.extend(ALL_PRETTY_MOE_ROUTES)