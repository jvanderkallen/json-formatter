import formatter
import ast

arr = ast.Array(
	ast.Literal('1'),
	ast.Literal('"foo"'),
	ast.Object(
		ast.Member('"foo"', ast.Literal('3'))
	),
	ast.Array(
		ast.Literal('"33"'),
		ast.Object(
			ast.Member('"foo"', ast.Object(
				ast.Member('"foo"', ast.Literal('3'))
			))
		)
	)
)

formatter.JsonFormatter(arr).print_formatted()

print('')
print('')

obj = ast.Object(
	ast.Member('"foo"', ast.Array(
	ast.Literal('1'),
		ast.Literal('"foo"'),
		ast.Object(
			ast.Member('"foo"', ast.Literal('3'))
		),
		ast.Array(
			ast.Literal('"33"'),
			ast.Object(ast.Member(
				'"foo"', ast.Object(ast.Member(
					'"foo"', ast.Literal('3')
				))
			))
		)
	))
)

formatter.JsonFormatter(obj).print_formatted()