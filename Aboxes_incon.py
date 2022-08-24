aboxes_inconsistent = ['a:A, a:-A',
'a:(A&-A)',
'a:(-A&A)',
'a:A, a:(-A&B)',
'a:A, a:(B&-A)',
'a:-A, a:(A&B)',
'a:-A, a:(B&A)',
'a:A, (b,a):r, b:/Ar.-A',
'a:-A, (b,a):r, b:/Ar.A',
'a:((A&-A)&B)',
'a:((-A&A)&B)',
'a:(B&(A&-A))',
'a:(B&(-A&A))',
'a:(A&(B&-A))',
'a:(A&(-A&B))',
'a:((B&-A)&A)',
'a:((-A&B)&A)',
'a:(-A&(B&A))',
'a:(-A&(A&B))',
'a:((B&A)&-A)',
'a:((A&B)&-A)',
'a:A, a:(-A&(B&C))',
'a:A, a:((B&C)&-A)',
'a:A, a:(B&(-A&C))',
'a:A, a:(B&(C&-A))',
'a:A, a:((-A&C)&B)',
'a:A, a:((C&-A)&B)',
'a:-A, a:(A&(B&C))',
'a:-A, a:((B&C)&A)',
'a:-A, a:(B&(A&C))',
'a:-A, a:(B&(C&A))',
'a:-A, a:((A&C)&B)',
'a:-A, a:((C&A)&B)',
'a:(A&C), a:(-A&B)',
'a:(C&A), a:(-A&B)',
'a:(A&C), a:(B&-A)',
'a:(C&A), a:(B&-A)',
'a:A, (c,b):r, (b,a):s, c:/Ar./As.-A',
'a:-A, (c,b):r, (b,a):s, c:/Ar./As.A',
'b:/Er.A, b:/Ar.-A',
'b:/Er.-A, b:/Ar.A',
'b:/Ar.A, (b,a):r, b:/Ar.-A',
'(c,a):s, c:/As.A, (b,a):r, b:/Ar.-A',
'a:A, (b,a):r, b:(B&/Ar.-A)',
'a:A, (b,a):r, b:(/Ar.-A&B)',
'a:-A, (b,a):r, b:(B&/Ar.A)',
'a:-A, (b,a):r, b:(/Ar.A&B)',
'a:A, (b,a):r, b:/Ar.(-A&B)',
'a:A, (b,a):r, b:/Ar.(B&-A)',
'a:-A, (b,a):r, b:/Ar.(A&B)',
'a:-A, (b,a):r, b:/Ar.(B&A)',
'a:(A&B), (b,a):r, b:/Ar.-A',
'a:(B&A), (b,a):r, b:/Ar.-A',
'a:(-A&B), (b,a):r, b:/Ar.A',
'a:(B&-A), (b,a):r, b:/Ar.A',
'a:(((A&-A)&B)&C)',
'a:(C&((A&-A)&B))',
'a:(((-A&A)&B)&C)',
'a:(C&((-A&A)&B))',
'a:((B&(A&-A))&C)',
'a:(C&(B&(A&-A)))',
'a:((B&(-A&A))&C)',
'a:(C&(B&(-A&A)))',
'a:(A&(B&(C&-A)))',
'a:(A&(B&(-A&C)))',
'a:(A&((C&-A)&B))',
'a:(A&((-A&C)&B))',
'a:((B&(C&-A))&A)',
'a:((B&(-A&C))&A)',
'a:(((C&-A)&B)&A)',
'a:(((-A&C)&B)&A)',
'a:(-A&(B&(C&A)))',
'a:(-A&(B&(A&C)))',
'a:(-A&((C&A)&B))',
'a:(-A&((A&C)&B))',
'a:((B&(C&A))&-A)',
'a:((B&(A&C))&-A)',
'a:(((C&A)&B)&-A)',
'a:(((A&C)&B)&-A)',
'a:(A&(-A&(B&C)))',
'a:(A&((B&C)&-A))',
'a:(-A&(A&(B&C)))',
'a:(-A&((B&C)&A))',
'a:((-A&(B&C))&A)',
'a:(((B&C)&-A)&A)',
'a:((A&(B&C))&-A)',
'a:(((B&C)&A)&-A)',
'a:A, a:(-A&(B&(C&D)))',
'a:A, a:((B&(C&D))&-A)',
'a:A, a:(-A&((C&D)&B))',
'a:A, a:(((C&D)&B)&-A)',
'a:A, a:(B&(-A&(C&D)))',
'a:A, a:(B&((C&D)&-A))',
'a:A, a:((-A&(C&D))&B)',
'a:A, a:(((C&D)&-A)&B)',
'a:A, a:(B&(C&(-A&D)))',
'a:A, a:(B&(C&(D&-A)))',
'a:A, a:((C&(-A&D))&B)',
'a:A, a:((C&(D&-A))&B)',
'a:A, a:(B&((-A&D)&C))',
'a:A, a:(B&((D&-A)&C))',
'a:A, a:(((-A&D)&C)&B)',
'a:A, a:(((D&-A)&C)&B)',
'a:-A, a:(A&(B&(C&D)))',
'a:-A, a:((B&(C&D))&A)',
'a:-A, a:(A&((C&D)&B))',
'a:-A, a:(((C&D)&B)&A)',
'a:-A, a:(B&(A&(C&D)))',
'a:-A, a:(B&((C&D)&A))',
'a:-A, a:((A&(C&D))&B)',
'a:-A, a:(((C&D)&A)&B)',
'a:-A, a:(B&(C&(A&D)))',
'a:-A, a:(B&(C&(D&A)))',
'a:-A, a:((C&(A&D))&B)',
'a:-A, a:((C&(D&A))&B)',
'a:-A, a:(B&((A&D)&C))',
'a:-A, a:(B&((D&A)&C))',
'a:-A, a:(((A&D)&C)&B)',
'a:-A, a:(((D&A)&C)&B)',
'a:(A&B), a:(-A&(C&D))',
'a:(A&B), a:((C&D)&-A)',
'a:(A&B), a:((-A&D)&C)',
'a:(A&B), a:((D&-A)&C)',
'a:(A&B), a:(C&(-A&D))',
'a:(A&B), a:(C&(D&-A))',
'a:(B&A), a:(-A&(C&D))',
'a:(B&A), a:((C&D)&-A)',
'a:(B&A), a:((-A&D)&C)',
'a:(B&A), a:((D&-A)&C)',
'a:(B&A), a:(C&(-A&D))',
'a:(B&A), a:(C&(D&-A))',
'a:(-A&B), a:(A&(C&D))',
'a:(-A&B), a:((C&D)&A)',
'a:(-A&B), a:((A&D)&C)',
'a:(-A&B), a:((D&A)&C)',
'a:(-A&B), a:(C&(A&D))',
'a:(-A&B), a:(C&(D&A))',
'a:(B&-A), a:(A&(C&D))',
'a:(B&-A), a:((C&D)&A)',
'a:(B&-A), a:((A&D)&C)',
'a:(B&-A), a:((D&A)&C)',
'a:(B&-A), a:(C&(A&D))',
'a:(B&-A), a:(C&(D&A))',
'a:A, (d,c):r, (c,b):s, (b,a):t, d:/Ar./As./At.-A',
'a:-A, (d,c):r, (c,b):s, (b,a):t, d:/Ar./As./At.A',
'(b,c):r, c:/Es.A, b:/Ar./As.-A',
'(b,c):r, c:/Es.-A, b:/Ar./As.A',
'b:/Ar./Es.A, (b,c):r, c:/As.-A',
'b:/Ar./Es.-A, (b,c):r, c:/As.A',
'(b,c):r, (c,a):s, c:/As.A, b:/Ar./As.-A',
'(b,c):r, (c,a):s, c:/As.-A, b:/Ar./As.A',
'a:A, (b,a):r, b:/Ar.((-A&B)&C)',
'a:A, (b,a):r, b:/Ar.((B&-A)&C)',
'a:A, (b,a):r, b:/Ar.(C&(-A&B))',
'a:A, (b,a):r, b:/Ar.(C&(B&-A))',
'a:-A, (b,a):r, b:/Ar.((A&B)&C)',
'a:-A, (b,a):r, b:/Ar.((B&A)&C)',
'a:-A, (b,a):r, b:/Ar.(C&(A&B))',
'a:-A, (b,a):r, b:/Ar.(C&(B&A))',
'a:A, (b,a):r, b:(C&/Ar.(-A&B))',
'a:A, (b,a):r, b:(/Ar.(-A&B)&C)',
'a:A, (b,a):r, b:(C&/Ar.(B&-A))',
'a:A, (b,a):r, b:(/Ar.(B&-A)&C)',
'a:-A, (b,a):r, b:(C&/Ar.(A&B))',
'a:-A, (b,a):r, b:(/Ar.(A&B)&C)',
'a:-A, (b,a):r, b:(C&/Ar.(B&A))',
'a:-A, (b,a):r, b:(/Ar.(B&A)&C)',
'a:A, (b,a):r, b:(B&(C&/Ar.-A))',
'a:A, (b,a):r, b:(B&(/Ar.-A&C))',
'a:A, (b,a):r, b:((C&/Ar.-A)&B)',
'a:A, (b,a):r, b:(/Ar.(-A&C)&B)',
'a:-A, (b,a):r, b:(B&(C&/Ar.A))',
'a:-A, (b,a):r, b:(B&(/Ar.A&C))',
'a:-A, (b,a):r, b:((C&/Ar.A)&B)',
'a:-A, (b,a):r, b:((/Ar.A&C)&B)',
'a:((A&B)&C), (b,a):r, b:/Ar.-A',
'a:(C&(A&B)), (b,a):r, b:/Ar.-A',
'a:(A&(B&C)), (b,a):r, b:/Ar.-A',
'a:((B&C)&A), (b,a):r, b:/Ar.-A',
'a:((-A&B)&C), (b,a):r, b:/Ar.A',
'a:(C&(-A&B)), (b,a):r, b:/Ar.A',
'a:(-A&(B&C)), (b,a):r, b:/Ar.A',
'a:((B&C)&-A), (b,a):r, b:/Ar.A',
'a:(A&B), (b,a):r, b:/Ar.(-A&B)',
'a:(A&B), (b,a):r, b:/Ar.(B&-A)',
'a:(B&A), (b,a):r, b:/Ar.(-A&B)',
'a:(B&A), (b,a):r, b:/Ar.(B&-A)',
'a:(-A&B), (b,a):r, b:/Ar.(A&B)',
'a:(-A&B), (b,a):r, b:/Ar.(B&A)',
'a:(B&-A), (b,a):r, b:/Ar.(A&B)',
'a:(B&-A), (b,a):r, b:/Ar.(B&A)',
'a:(A&B), (b,a):r, b:(C&/Ar.-A)',
'a:(A&B), (b,a):r, b:(/Ar.-A&C)',
'a:(B&A), (b,a):r, b:(C&/Ar.-A)',
'a:(B&A), (b,a):r, b:(/Ar.-A&C)',
'a:(-A&B), (b,a):r, b:(C&/Ar.A)',
'a:(-A&B), (b,a):r, b:(/Ar.A&C)',
'a:(B&-A), (b,a):r, b:(C&/Ar.A)',
'a:(B&-A), (b,a):r, b:(/Ar.A&C)',
'a:A, (c,b):r, (b,a):s, c:(B&/Ar./As.-A)',
'a:A, (c,b):r, (b,a):s, c:(/Ar./As.-A&B)',
'a:-A, (c,b):r, (b,a):s, c:(B&/Ar./As.A)',
'a:-A, (c,b):r, (b,a):s, c:(/Ar./As.A&B)',
'a:A, (c,b):r, (b,a):s, c:/Ar./As.(B&-A)',
'a:A, (c,b):r, (b,a):s, c:/Ar./As.(-A&B)',
'a:-A, (c,b):r, (b,a):s, c:/Ar./As.(B&A)',
'a:-A, (c,b):r, (b,a):s, c:/Ar./As.(A&B)',
'a:(A&B), (c,b):r, (b,a):s, c:/Ar./As.-A',
'a:(B&A), (c,b):r, (b,a):s, c:/Ar./As.-A',
'a:(-A&B), (c,b):r, (b,a):s, c:/Ar./As.A',
'a:(B&-A), (c,b):r, (b,a):s, c:/Ar./As.A',
'a:A, (c,b):r, (b,a):s, c:/Ar.(B&/As.-A)',
'a:A, (c,b):r, (b,a):s, c:/Ar.(/As.-A&B)',
'a:-A, (c,b):r, (b,a):s, c:/Ar.(B&/As.A)',
'a:-A, (c,b):r, (b,a):s, c:/Ar.(/As.A&B)',
'b:(/Er.A&/Ar.-A)',
'b:(/Er.-A&/Ar.A)',
'b:(/Ar.-A&/Er.A)',
'b:(/Ar.A&/Er.-A)',
'b:/Er.-A, b:/Ar.(A&B)',
'b:/Er.-A, b:/Ar.(B&A)',
'b:/Er.(-A&B), b:/Ar.A',
'b:/Er.(B&-A), b:/Ar.A',
'b:/Er.A, b:/Ar.(-A&B)',
'b:/Er.A, b:/Ar.(B&-A)',
'b:/Er.(A&B), b:/Ar.-A',
'b:/Er.(B&A), b:/Ar.-A',
'b:/Er.A, b:(B&/Ar.-A)',
'b:/Er.A, b:(/Ar.-A&B)',
'b:/Er.-A, b:(B&/Ar.A)',
'b:/Er.-A, b:(/Ar.A&B)',
'b:(B&/Er.A), b:/Ar.-A',
'b:(/Er.A&B), b:/Ar.-A',
'b:(B&/Er.-A), b:/Ar.A',
'b:(/Er.-A&B), b:/Ar.A']
