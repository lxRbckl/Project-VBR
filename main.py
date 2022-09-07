# Project RB8 by Alex Arbuckle #


# import <
from pandas import DataFrame
import dash_bootstrap_components as dbc
from dash import dcc, html, Dash, Input, State, Output, dash_table

# >


# global <
gFeature = {

    'rev' : {

        'min' : 0,
        'max' : 50,
        'value' : 20,
        'name' : '# Revolution'

    },
    'spin' : {

        'min' : 0,
        'max' : 5,
        'value' : 3,
        'name' : '# Spin'

    }

}
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

                # input <
                # datatable <
                # graph <
                dbc.Row(

                    justify = 'between',
                    style = dict(margin = '5%'),
                    children = [

                        dbc.Col(

                            width = 'auto',
                            children = [

                                # label <
                                # input <
                                dbc.Label(

                                    style = dict(fontSize = 15),
                                    children = gFeature[k]['name']

                                ),
                                dbc.Input(
                                    step = 1,
                                    id = f'{k}Id',
                                    type = 'number',
                                    min = gFeature[k]['min'],
                                    max = gFeature[k]['max'],
                                    value = gFeature[k]['value'],
                                    style = dict(padding = '3%', fontSize = 15)

                                )

                                # >

                            ]

                        )

                    for k in gFeature.keys()]

                ),
                dbc.Col(

                    width = 'auto',
                    align = 'center',
                    id = 'colDatatableId'

                ),
                dbc.Col(

                    width = 'auto',
                    align = 'center',
                    id = 'colGraphId'

                )

                # >

            ]

        )

    )


@application.callback(

    Output('colDatatableId', 'children'),
    Input('revId', 'value'),
    Input('spinId', 'value')

)
def datatableCallback(pRevValue: int, pSpinValue: int):
    '''  '''

    d = {

        'Revolution' : [(r + 1) for r in range(pRevValue)],
        **{f'Spin {s + 1}' : [None for r in range(pRevValue)] for s in range(pSpinValue)}

    }

    return dash_table.DataTable(

        editable = True,
        id = 'datatableId',
        row_deletable = True,
        style_data = dict(textAlign = 'center'),
        style_header = dict(paddingLeft = 15, paddingRight = 15),
        data = [{k : d[k][i] for k in d.keys()} for i in range(pRevValue)],
        columns = [{'id' : k, 'name' : k, 'deletable' : True} for k in d.keys()]

    )


@application.callback(

    Output('colGraphId', 'children'),
    Input('datatableId', 'data')

)
def graphCallback(pDatatableData: list):
    '''  '''

    df = DataFrame(pDatatableData)
    return [

        dcc.Graph(

            figure = {

                'data' : [{

                    'y' : df[k],
                    'type' : 'bar',
                    'text' : df[k],
                    'x' : df['Revolution']

                }],
                'layout' : {

                    'width' : 600,
                    'height' : 150,
                    'margin' : {'t' : 0, 'b' : 0},
                    'padding' : {'t' : 1, 'l' : 9, 'r' : 1},
                    'xaxis' : {

                        'dtick' : 1,
                        'gridwidth' : 0.5,
                        'automargin' : True,
                        'showticklabels' : True

                    },
                    'yaxis' : {

                        'dtick' : 0.5,
                        'gridwidth' : 0.5,
                        'automargin' : True,
                        'title' : {'text' : k},
                        'showticklabels' : True,

                    }

                }

            }

        )

    for k in list(pDatatableData[0].keys())[1:]]


# main <
if (__name__ == '__main__'):

    application.layout = layoutFunction()
    application.run_server(debug = True)

# >
