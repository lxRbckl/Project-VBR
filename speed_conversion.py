# import <
import dash_bootstrap_components as dbc
from dash import dcc, html, Dash, Input, State, Output, dash_table

# >


# global <
application = Dash(

    external_stylesheets = [dbc.themes.GRID]

)

# >


def layoutFunction():
    '''  '''

    return dbc.Container(

        children = dbc.Row(

            justify = 'between',
            children = [

                # <
                # <
                # <
                dbc.Row(

                    justify = 'between',
                    style = dict(margin = '5%'),
                    children = [

                        #

                    ]

                ),
                dbc.Col(

                    width = 'auto',
                    align = 'center',
                    id = 'colDatatableInputId'

                ),
                dbc.Col(

                    width = 'auto',
                    align = 'center',
                    id = 'colDatatableOutputId'

                )

                # >

            ]

        )

    )
