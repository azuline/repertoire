-- admin token: b'b\xec$\xe7\xd7\r:U\xdf\xd8#\xb8\x00j\xd8\xc6\xdd\xa2j\xec\x91\x93\xef\xc0\xc8>5\xce\x8a\x96\x8b\xc8'
-- azul token: b'I\xef\xdaW\x85\x12\x01]@d\xb8\xa3\xf2\xb2h\x98\xd8jHV=\x13\x96\x0cGL`\xda\xa9\x1c\xa79'
INSERT INTO system__users (id, username, token_prefix, token_hash)
	VALUES (1, "admin", X'62ec24e7d70d3a55dfd823b8', 'pbkdf2:sha256:150000$0lH2wS00$28cd8fb44dade0da081f610ade308e9528ec0b0cb7cdc697b4d20406bb201410'),
		   (2, "azul", X'49efda578512015d4064b8a3', 'pbkdf2:sha256:150000$k5k6W67S$3f66aefff48854f37d70b983aaf695d4094a895296177fb677c13d48444659be');
