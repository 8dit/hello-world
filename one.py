try
{	FILE *f;
	f = fopen("newdocument.txt","w"); "r"  "a" 
	fprintf(f,"hello world");
	fclose(f);
	
	f = fopen("newdocument.txt","r");
	fscanf(f,"%d",&num);
	fclose(f);
}
catch(int x)
{
}