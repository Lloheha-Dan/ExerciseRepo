#!/usr/bin/awk -f
BEGIN { FS="\t";OFS="_";
}
{ count++; if($1 != "#")
  {
print "Currently doing "count ; total=total + ($12 * $3)
  }
}
END{
print "The total for "count" lines was " int(total) > "awkoutputfile.txt"
print "Script run complete." >>"awkoutputfile.txt"
system("ls -alrt *awk*")
}
