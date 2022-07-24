<HTML>
<HEAD>
<TITLE>Authorization</TITLE>
</HEAD>
<BODY bgcolor="#f5ffd9">
<H2 align="center">Authorization</H2>
<HR size="4">
<CENTER>
<TABLE border="1">
  <TR>
    <TD>You need to enter a user ID and password to download the PDF file. The user ID and password are notified to workshop participants in the email from the organizer. </TD></TR>
</TABLE>
</CENTER>
<CENTER>
<TABLE height="143">
  <TR>
    <TD align="center"><BR>
    <FORM action="ezpsw.cgi" method="POST">
    <INPUT type="hidden" name="action" value="ninshou">
<B>ID:</B><INPUT name="id" size="30"><BR>
<B>Password:</B><INPUT type="password" name="psw" size="21"><BR>
<BR>
<INPUT type="submit" value="Submit "><INPUT type="reset" value="RESET">
    </FORM>
</TD></TR>
</TABLE>
</CENTER>
<HR width="80%">

<!--
<CENTER>
<TABLE>
  <TR>
    <TD align="center"><FONT size="+1"><B>New Account</B></FONT><BR>
    <FORM action="ezpsw.cgi" method="POST">
    <INPUT type="hidden" name="action" value="sakusei">
<B>ID</B><INPUT name="id" size="30"><BR>
<B>Mail Address</B><INPUT name="mail_add" size="30"><BR>
<BR>
<INPUT type="submit" value="Submit "><INPUT type="reset" value="RESET">
    </FORM>
</TABLE>
</CENTER>
-->

<TABLE width="100%">
  <TR>
    <TD align="left" valign="top"><FONT size="+1"><A href="http://www.digitalcity.jst.go.jp/conferences/20030919_crest-program.html">BACK</A></FONT></TD>
    <TD align="right" valign="top">
    <FORM action="ezpsw.cgi" method="POST">
    <INPUT type="hidden" name="action" value="go_admin">
<INPUT type="submit" value="Administraator"><INPUT type="password" name="pass" size="15">
    </FORM>
</TD></TR>
</TABLE>
<H4 align=right>
<A href="http://www.net-easy.com/">
EASY PSW Ver1.0</A></H4>
</BODY>
</HTML>
