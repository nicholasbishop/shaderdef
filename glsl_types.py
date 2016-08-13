from typing import Any

def is_scalar(var: Any) -> bool:
    return isinstance(var, (bool, int, uint, float, double))
class uint:
    def __init__(self, val: int=0) -> None:
        self._val = val
class double:
    def __init__(self, val: float=0.0) -> None:
        self._val = val
class bvec2:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = False
            self._y = False
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> "bvec2":
        return bvec2(self._x, self._x)
    @property
    def xy(self) -> "bvec2":
        return bvec2(self._x, self._y)
    @property
    def yy(self) -> "bvec2":
        return bvec2(self._y, self._y)
class bvec3:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = False
            self._y = False
            self._z = False
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> bvec2:
        return bvec2(self._x, self._x)
    @property
    def xy(self) -> bvec2:
        return bvec2(self._x, self._y)
    @property
    def xz(self) -> bvec2:
        return bvec2(self._x, self._z)
    @property
    def yy(self) -> bvec2:
        return bvec2(self._y, self._y)
    @property
    def yz(self) -> bvec2:
        return bvec2(self._y, self._z)
    @property
    def zz(self) -> bvec2:
        return bvec2(self._z, self._z)
    @property
    def xxx(self) -> "bvec3":
        return bvec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> "bvec3":
        return bvec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> "bvec3":
        return bvec3(self._x, self._x, self._z)
    @property
    def xyy(self) -> "bvec3":
        return bvec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> "bvec3":
        return bvec3(self._x, self._y, self._z)
    @property
    def xzz(self) -> "bvec3":
        return bvec3(self._x, self._z, self._z)
    @property
    def yyy(self) -> "bvec3":
        return bvec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> "bvec3":
        return bvec3(self._y, self._y, self._z)
    @property
    def yzz(self) -> "bvec3":
        return bvec3(self._y, self._z, self._z)
    @property
    def zzz(self) -> "bvec3":
        return bvec3(self._z, self._z, self._z)
class bvec4:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = False
            self._y = False
            self._z = False
            self._w = False
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> bvec2:
        return bvec2(self._x, self._x)
    @property
    def xy(self) -> bvec2:
        return bvec2(self._x, self._y)
    @property
    def xz(self) -> bvec2:
        return bvec2(self._x, self._z)
    @property
    def xw(self) -> bvec2:
        return bvec2(self._x, self._w)
    @property
    def yy(self) -> bvec2:
        return bvec2(self._y, self._y)
    @property
    def yz(self) -> bvec2:
        return bvec2(self._y, self._z)
    @property
    def yw(self) -> bvec2:
        return bvec2(self._y, self._w)
    @property
    def zz(self) -> bvec2:
        return bvec2(self._z, self._z)
    @property
    def zw(self) -> bvec2:
        return bvec2(self._z, self._w)
    @property
    def ww(self) -> bvec2:
        return bvec2(self._w, self._w)
    @property
    def xxx(self) -> bvec3:
        return bvec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> bvec3:
        return bvec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> bvec3:
        return bvec3(self._x, self._x, self._z)
    @property
    def xxw(self) -> bvec3:
        return bvec3(self._x, self._x, self._w)
    @property
    def xyy(self) -> bvec3:
        return bvec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> bvec3:
        return bvec3(self._x, self._y, self._z)
    @property
    def xyw(self) -> bvec3:
        return bvec3(self._x, self._y, self._w)
    @property
    def xzz(self) -> bvec3:
        return bvec3(self._x, self._z, self._z)
    @property
    def xzw(self) -> bvec3:
        return bvec3(self._x, self._z, self._w)
    @property
    def xww(self) -> bvec3:
        return bvec3(self._x, self._w, self._w)
    @property
    def yyy(self) -> bvec3:
        return bvec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> bvec3:
        return bvec3(self._y, self._y, self._z)
    @property
    def yyw(self) -> bvec3:
        return bvec3(self._y, self._y, self._w)
    @property
    def yzz(self) -> bvec3:
        return bvec3(self._y, self._z, self._z)
    @property
    def yzw(self) -> bvec3:
        return bvec3(self._y, self._z, self._w)
    @property
    def yww(self) -> bvec3:
        return bvec3(self._y, self._w, self._w)
    @property
    def zzz(self) -> bvec3:
        return bvec3(self._z, self._z, self._z)
    @property
    def zzw(self) -> bvec3:
        return bvec3(self._z, self._z, self._w)
    @property
    def zww(self) -> bvec3:
        return bvec3(self._z, self._w, self._w)
    @property
    def www(self) -> bvec3:
        return bvec3(self._w, self._w, self._w)
    @property
    def xxxx(self) -> "bvec4":
        return bvec4(self._x, self._x, self._x, self._x)
    @property
    def xxxy(self) -> "bvec4":
        return bvec4(self._x, self._x, self._x, self._y)
    @property
    def xxxz(self) -> "bvec4":
        return bvec4(self._x, self._x, self._x, self._z)
    @property
    def xxxw(self) -> "bvec4":
        return bvec4(self._x, self._x, self._x, self._w)
    @property
    def xxyy(self) -> "bvec4":
        return bvec4(self._x, self._x, self._y, self._y)
    @property
    def xxyz(self) -> "bvec4":
        return bvec4(self._x, self._x, self._y, self._z)
    @property
    def xxyw(self) -> "bvec4":
        return bvec4(self._x, self._x, self._y, self._w)
    @property
    def xxzz(self) -> "bvec4":
        return bvec4(self._x, self._x, self._z, self._z)
    @property
    def xxzw(self) -> "bvec4":
        return bvec4(self._x, self._x, self._z, self._w)
    @property
    def xxww(self) -> "bvec4":
        return bvec4(self._x, self._x, self._w, self._w)
    @property
    def xyyy(self) -> "bvec4":
        return bvec4(self._x, self._y, self._y, self._y)
    @property
    def xyyz(self) -> "bvec4":
        return bvec4(self._x, self._y, self._y, self._z)
    @property
    def xyyw(self) -> "bvec4":
        return bvec4(self._x, self._y, self._y, self._w)
    @property
    def xyzz(self) -> "bvec4":
        return bvec4(self._x, self._y, self._z, self._z)
    @property
    def xyzw(self) -> "bvec4":
        return bvec4(self._x, self._y, self._z, self._w)
    @property
    def xyww(self) -> "bvec4":
        return bvec4(self._x, self._y, self._w, self._w)
    @property
    def xzzz(self) -> "bvec4":
        return bvec4(self._x, self._z, self._z, self._z)
    @property
    def xzzw(self) -> "bvec4":
        return bvec4(self._x, self._z, self._z, self._w)
    @property
    def xzww(self) -> "bvec4":
        return bvec4(self._x, self._z, self._w, self._w)
    @property
    def xwww(self) -> "bvec4":
        return bvec4(self._x, self._w, self._w, self._w)
    @property
    def yyyy(self) -> "bvec4":
        return bvec4(self._y, self._y, self._y, self._y)
    @property
    def yyyz(self) -> "bvec4":
        return bvec4(self._y, self._y, self._y, self._z)
    @property
    def yyyw(self) -> "bvec4":
        return bvec4(self._y, self._y, self._y, self._w)
    @property
    def yyzz(self) -> "bvec4":
        return bvec4(self._y, self._y, self._z, self._z)
    @property
    def yyzw(self) -> "bvec4":
        return bvec4(self._y, self._y, self._z, self._w)
    @property
    def yyww(self) -> "bvec4":
        return bvec4(self._y, self._y, self._w, self._w)
    @property
    def yzzz(self) -> "bvec4":
        return bvec4(self._y, self._z, self._z, self._z)
    @property
    def yzzw(self) -> "bvec4":
        return bvec4(self._y, self._z, self._z, self._w)
    @property
    def yzww(self) -> "bvec4":
        return bvec4(self._y, self._z, self._w, self._w)
    @property
    def ywww(self) -> "bvec4":
        return bvec4(self._y, self._w, self._w, self._w)
    @property
    def zzzz(self) -> "bvec4":
        return bvec4(self._z, self._z, self._z, self._z)
    @property
    def zzzw(self) -> "bvec4":
        return bvec4(self._z, self._z, self._z, self._w)
    @property
    def zzww(self) -> "bvec4":
        return bvec4(self._z, self._z, self._w, self._w)
    @property
    def zwww(self) -> "bvec4":
        return bvec4(self._z, self._w, self._w, self._w)
    @property
    def wwww(self) -> "bvec4":
        return bvec4(self._w, self._w, self._w, self._w)
class ivec2:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0
            self._y = 0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> "ivec2":
        return ivec2(self._x, self._x)
    @property
    def xy(self) -> "ivec2":
        return ivec2(self._x, self._y)
    @property
    def yy(self) -> "ivec2":
        return ivec2(self._y, self._y)
class ivec3:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0
            self._y = 0
            self._z = 0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> ivec2:
        return ivec2(self._x, self._x)
    @property
    def xy(self) -> ivec2:
        return ivec2(self._x, self._y)
    @property
    def xz(self) -> ivec2:
        return ivec2(self._x, self._z)
    @property
    def yy(self) -> ivec2:
        return ivec2(self._y, self._y)
    @property
    def yz(self) -> ivec2:
        return ivec2(self._y, self._z)
    @property
    def zz(self) -> ivec2:
        return ivec2(self._z, self._z)
    @property
    def xxx(self) -> "ivec3":
        return ivec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> "ivec3":
        return ivec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> "ivec3":
        return ivec3(self._x, self._x, self._z)
    @property
    def xyy(self) -> "ivec3":
        return ivec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> "ivec3":
        return ivec3(self._x, self._y, self._z)
    @property
    def xzz(self) -> "ivec3":
        return ivec3(self._x, self._z, self._z)
    @property
    def yyy(self) -> "ivec3":
        return ivec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> "ivec3":
        return ivec3(self._y, self._y, self._z)
    @property
    def yzz(self) -> "ivec3":
        return ivec3(self._y, self._z, self._z)
    @property
    def zzz(self) -> "ivec3":
        return ivec3(self._z, self._z, self._z)
class ivec4:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0
            self._y = 0
            self._z = 0
            self._w = 0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> ivec2:
        return ivec2(self._x, self._x)
    @property
    def xy(self) -> ivec2:
        return ivec2(self._x, self._y)
    @property
    def xz(self) -> ivec2:
        return ivec2(self._x, self._z)
    @property
    def xw(self) -> ivec2:
        return ivec2(self._x, self._w)
    @property
    def yy(self) -> ivec2:
        return ivec2(self._y, self._y)
    @property
    def yz(self) -> ivec2:
        return ivec2(self._y, self._z)
    @property
    def yw(self) -> ivec2:
        return ivec2(self._y, self._w)
    @property
    def zz(self) -> ivec2:
        return ivec2(self._z, self._z)
    @property
    def zw(self) -> ivec2:
        return ivec2(self._z, self._w)
    @property
    def ww(self) -> ivec2:
        return ivec2(self._w, self._w)
    @property
    def xxx(self) -> ivec3:
        return ivec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> ivec3:
        return ivec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> ivec3:
        return ivec3(self._x, self._x, self._z)
    @property
    def xxw(self) -> ivec3:
        return ivec3(self._x, self._x, self._w)
    @property
    def xyy(self) -> ivec3:
        return ivec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> ivec3:
        return ivec3(self._x, self._y, self._z)
    @property
    def xyw(self) -> ivec3:
        return ivec3(self._x, self._y, self._w)
    @property
    def xzz(self) -> ivec3:
        return ivec3(self._x, self._z, self._z)
    @property
    def xzw(self) -> ivec3:
        return ivec3(self._x, self._z, self._w)
    @property
    def xww(self) -> ivec3:
        return ivec3(self._x, self._w, self._w)
    @property
    def yyy(self) -> ivec3:
        return ivec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> ivec3:
        return ivec3(self._y, self._y, self._z)
    @property
    def yyw(self) -> ivec3:
        return ivec3(self._y, self._y, self._w)
    @property
    def yzz(self) -> ivec3:
        return ivec3(self._y, self._z, self._z)
    @property
    def yzw(self) -> ivec3:
        return ivec3(self._y, self._z, self._w)
    @property
    def yww(self) -> ivec3:
        return ivec3(self._y, self._w, self._w)
    @property
    def zzz(self) -> ivec3:
        return ivec3(self._z, self._z, self._z)
    @property
    def zzw(self) -> ivec3:
        return ivec3(self._z, self._z, self._w)
    @property
    def zww(self) -> ivec3:
        return ivec3(self._z, self._w, self._w)
    @property
    def www(self) -> ivec3:
        return ivec3(self._w, self._w, self._w)
    @property
    def xxxx(self) -> "ivec4":
        return ivec4(self._x, self._x, self._x, self._x)
    @property
    def xxxy(self) -> "ivec4":
        return ivec4(self._x, self._x, self._x, self._y)
    @property
    def xxxz(self) -> "ivec4":
        return ivec4(self._x, self._x, self._x, self._z)
    @property
    def xxxw(self) -> "ivec4":
        return ivec4(self._x, self._x, self._x, self._w)
    @property
    def xxyy(self) -> "ivec4":
        return ivec4(self._x, self._x, self._y, self._y)
    @property
    def xxyz(self) -> "ivec4":
        return ivec4(self._x, self._x, self._y, self._z)
    @property
    def xxyw(self) -> "ivec4":
        return ivec4(self._x, self._x, self._y, self._w)
    @property
    def xxzz(self) -> "ivec4":
        return ivec4(self._x, self._x, self._z, self._z)
    @property
    def xxzw(self) -> "ivec4":
        return ivec4(self._x, self._x, self._z, self._w)
    @property
    def xxww(self) -> "ivec4":
        return ivec4(self._x, self._x, self._w, self._w)
    @property
    def xyyy(self) -> "ivec4":
        return ivec4(self._x, self._y, self._y, self._y)
    @property
    def xyyz(self) -> "ivec4":
        return ivec4(self._x, self._y, self._y, self._z)
    @property
    def xyyw(self) -> "ivec4":
        return ivec4(self._x, self._y, self._y, self._w)
    @property
    def xyzz(self) -> "ivec4":
        return ivec4(self._x, self._y, self._z, self._z)
    @property
    def xyzw(self) -> "ivec4":
        return ivec4(self._x, self._y, self._z, self._w)
    @property
    def xyww(self) -> "ivec4":
        return ivec4(self._x, self._y, self._w, self._w)
    @property
    def xzzz(self) -> "ivec4":
        return ivec4(self._x, self._z, self._z, self._z)
    @property
    def xzzw(self) -> "ivec4":
        return ivec4(self._x, self._z, self._z, self._w)
    @property
    def xzww(self) -> "ivec4":
        return ivec4(self._x, self._z, self._w, self._w)
    @property
    def xwww(self) -> "ivec4":
        return ivec4(self._x, self._w, self._w, self._w)
    @property
    def yyyy(self) -> "ivec4":
        return ivec4(self._y, self._y, self._y, self._y)
    @property
    def yyyz(self) -> "ivec4":
        return ivec4(self._y, self._y, self._y, self._z)
    @property
    def yyyw(self) -> "ivec4":
        return ivec4(self._y, self._y, self._y, self._w)
    @property
    def yyzz(self) -> "ivec4":
        return ivec4(self._y, self._y, self._z, self._z)
    @property
    def yyzw(self) -> "ivec4":
        return ivec4(self._y, self._y, self._z, self._w)
    @property
    def yyww(self) -> "ivec4":
        return ivec4(self._y, self._y, self._w, self._w)
    @property
    def yzzz(self) -> "ivec4":
        return ivec4(self._y, self._z, self._z, self._z)
    @property
    def yzzw(self) -> "ivec4":
        return ivec4(self._y, self._z, self._z, self._w)
    @property
    def yzww(self) -> "ivec4":
        return ivec4(self._y, self._z, self._w, self._w)
    @property
    def ywww(self) -> "ivec4":
        return ivec4(self._y, self._w, self._w, self._w)
    @property
    def zzzz(self) -> "ivec4":
        return ivec4(self._z, self._z, self._z, self._z)
    @property
    def zzzw(self) -> "ivec4":
        return ivec4(self._z, self._z, self._z, self._w)
    @property
    def zzww(self) -> "ivec4":
        return ivec4(self._z, self._z, self._w, self._w)
    @property
    def zwww(self) -> "ivec4":
        return ivec4(self._z, self._w, self._w, self._w)
    @property
    def wwww(self) -> "ivec4":
        return ivec4(self._w, self._w, self._w, self._w)
class uvec2:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0
            self._y = 0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> "uvec2":
        return uvec2(self._x, self._x)
    @property
    def xy(self) -> "uvec2":
        return uvec2(self._x, self._y)
    @property
    def yy(self) -> "uvec2":
        return uvec2(self._y, self._y)
class uvec3:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0
            self._y = 0
            self._z = 0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> uvec2:
        return uvec2(self._x, self._x)
    @property
    def xy(self) -> uvec2:
        return uvec2(self._x, self._y)
    @property
    def xz(self) -> uvec2:
        return uvec2(self._x, self._z)
    @property
    def yy(self) -> uvec2:
        return uvec2(self._y, self._y)
    @property
    def yz(self) -> uvec2:
        return uvec2(self._y, self._z)
    @property
    def zz(self) -> uvec2:
        return uvec2(self._z, self._z)
    @property
    def xxx(self) -> "uvec3":
        return uvec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> "uvec3":
        return uvec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> "uvec3":
        return uvec3(self._x, self._x, self._z)
    @property
    def xyy(self) -> "uvec3":
        return uvec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> "uvec3":
        return uvec3(self._x, self._y, self._z)
    @property
    def xzz(self) -> "uvec3":
        return uvec3(self._x, self._z, self._z)
    @property
    def yyy(self) -> "uvec3":
        return uvec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> "uvec3":
        return uvec3(self._y, self._y, self._z)
    @property
    def yzz(self) -> "uvec3":
        return uvec3(self._y, self._z, self._z)
    @property
    def zzz(self) -> "uvec3":
        return uvec3(self._z, self._z, self._z)
class uvec4:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0
            self._y = 0
            self._z = 0
            self._w = 0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> uvec2:
        return uvec2(self._x, self._x)
    @property
    def xy(self) -> uvec2:
        return uvec2(self._x, self._y)
    @property
    def xz(self) -> uvec2:
        return uvec2(self._x, self._z)
    @property
    def xw(self) -> uvec2:
        return uvec2(self._x, self._w)
    @property
    def yy(self) -> uvec2:
        return uvec2(self._y, self._y)
    @property
    def yz(self) -> uvec2:
        return uvec2(self._y, self._z)
    @property
    def yw(self) -> uvec2:
        return uvec2(self._y, self._w)
    @property
    def zz(self) -> uvec2:
        return uvec2(self._z, self._z)
    @property
    def zw(self) -> uvec2:
        return uvec2(self._z, self._w)
    @property
    def ww(self) -> uvec2:
        return uvec2(self._w, self._w)
    @property
    def xxx(self) -> uvec3:
        return uvec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> uvec3:
        return uvec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> uvec3:
        return uvec3(self._x, self._x, self._z)
    @property
    def xxw(self) -> uvec3:
        return uvec3(self._x, self._x, self._w)
    @property
    def xyy(self) -> uvec3:
        return uvec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> uvec3:
        return uvec3(self._x, self._y, self._z)
    @property
    def xyw(self) -> uvec3:
        return uvec3(self._x, self._y, self._w)
    @property
    def xzz(self) -> uvec3:
        return uvec3(self._x, self._z, self._z)
    @property
    def xzw(self) -> uvec3:
        return uvec3(self._x, self._z, self._w)
    @property
    def xww(self) -> uvec3:
        return uvec3(self._x, self._w, self._w)
    @property
    def yyy(self) -> uvec3:
        return uvec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> uvec3:
        return uvec3(self._y, self._y, self._z)
    @property
    def yyw(self) -> uvec3:
        return uvec3(self._y, self._y, self._w)
    @property
    def yzz(self) -> uvec3:
        return uvec3(self._y, self._z, self._z)
    @property
    def yzw(self) -> uvec3:
        return uvec3(self._y, self._z, self._w)
    @property
    def yww(self) -> uvec3:
        return uvec3(self._y, self._w, self._w)
    @property
    def zzz(self) -> uvec3:
        return uvec3(self._z, self._z, self._z)
    @property
    def zzw(self) -> uvec3:
        return uvec3(self._z, self._z, self._w)
    @property
    def zww(self) -> uvec3:
        return uvec3(self._z, self._w, self._w)
    @property
    def www(self) -> uvec3:
        return uvec3(self._w, self._w, self._w)
    @property
    def xxxx(self) -> "uvec4":
        return uvec4(self._x, self._x, self._x, self._x)
    @property
    def xxxy(self) -> "uvec4":
        return uvec4(self._x, self._x, self._x, self._y)
    @property
    def xxxz(self) -> "uvec4":
        return uvec4(self._x, self._x, self._x, self._z)
    @property
    def xxxw(self) -> "uvec4":
        return uvec4(self._x, self._x, self._x, self._w)
    @property
    def xxyy(self) -> "uvec4":
        return uvec4(self._x, self._x, self._y, self._y)
    @property
    def xxyz(self) -> "uvec4":
        return uvec4(self._x, self._x, self._y, self._z)
    @property
    def xxyw(self) -> "uvec4":
        return uvec4(self._x, self._x, self._y, self._w)
    @property
    def xxzz(self) -> "uvec4":
        return uvec4(self._x, self._x, self._z, self._z)
    @property
    def xxzw(self) -> "uvec4":
        return uvec4(self._x, self._x, self._z, self._w)
    @property
    def xxww(self) -> "uvec4":
        return uvec4(self._x, self._x, self._w, self._w)
    @property
    def xyyy(self) -> "uvec4":
        return uvec4(self._x, self._y, self._y, self._y)
    @property
    def xyyz(self) -> "uvec4":
        return uvec4(self._x, self._y, self._y, self._z)
    @property
    def xyyw(self) -> "uvec4":
        return uvec4(self._x, self._y, self._y, self._w)
    @property
    def xyzz(self) -> "uvec4":
        return uvec4(self._x, self._y, self._z, self._z)
    @property
    def xyzw(self) -> "uvec4":
        return uvec4(self._x, self._y, self._z, self._w)
    @property
    def xyww(self) -> "uvec4":
        return uvec4(self._x, self._y, self._w, self._w)
    @property
    def xzzz(self) -> "uvec4":
        return uvec4(self._x, self._z, self._z, self._z)
    @property
    def xzzw(self) -> "uvec4":
        return uvec4(self._x, self._z, self._z, self._w)
    @property
    def xzww(self) -> "uvec4":
        return uvec4(self._x, self._z, self._w, self._w)
    @property
    def xwww(self) -> "uvec4":
        return uvec4(self._x, self._w, self._w, self._w)
    @property
    def yyyy(self) -> "uvec4":
        return uvec4(self._y, self._y, self._y, self._y)
    @property
    def yyyz(self) -> "uvec4":
        return uvec4(self._y, self._y, self._y, self._z)
    @property
    def yyyw(self) -> "uvec4":
        return uvec4(self._y, self._y, self._y, self._w)
    @property
    def yyzz(self) -> "uvec4":
        return uvec4(self._y, self._y, self._z, self._z)
    @property
    def yyzw(self) -> "uvec4":
        return uvec4(self._y, self._y, self._z, self._w)
    @property
    def yyww(self) -> "uvec4":
        return uvec4(self._y, self._y, self._w, self._w)
    @property
    def yzzz(self) -> "uvec4":
        return uvec4(self._y, self._z, self._z, self._z)
    @property
    def yzzw(self) -> "uvec4":
        return uvec4(self._y, self._z, self._z, self._w)
    @property
    def yzww(self) -> "uvec4":
        return uvec4(self._y, self._z, self._w, self._w)
    @property
    def ywww(self) -> "uvec4":
        return uvec4(self._y, self._w, self._w, self._w)
    @property
    def zzzz(self) -> "uvec4":
        return uvec4(self._z, self._z, self._z, self._z)
    @property
    def zzzw(self) -> "uvec4":
        return uvec4(self._z, self._z, self._z, self._w)
    @property
    def zzww(self) -> "uvec4":
        return uvec4(self._z, self._z, self._w, self._w)
    @property
    def zwww(self) -> "uvec4":
        return uvec4(self._z, self._w, self._w, self._w)
    @property
    def wwww(self) -> "uvec4":
        return uvec4(self._w, self._w, self._w, self._w)
class vec2:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0.0
            self._y = 0.0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> "vec2":
        return vec2(self._x, self._x)
    @property
    def xy(self) -> "vec2":
        return vec2(self._x, self._y)
    @property
    def yy(self) -> "vec2":
        return vec2(self._y, self._y)
class vec3:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> vec2:
        return vec2(self._x, self._x)
    @property
    def xy(self) -> vec2:
        return vec2(self._x, self._y)
    @property
    def xz(self) -> vec2:
        return vec2(self._x, self._z)
    @property
    def yy(self) -> vec2:
        return vec2(self._y, self._y)
    @property
    def yz(self) -> vec2:
        return vec2(self._y, self._z)
    @property
    def zz(self) -> vec2:
        return vec2(self._z, self._z)
    @property
    def xxx(self) -> "vec3":
        return vec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> "vec3":
        return vec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> "vec3":
        return vec3(self._x, self._x, self._z)
    @property
    def xyy(self) -> "vec3":
        return vec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> "vec3":
        return vec3(self._x, self._y, self._z)
    @property
    def xzz(self) -> "vec3":
        return vec3(self._x, self._z, self._z)
    @property
    def yyy(self) -> "vec3":
        return vec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> "vec3":
        return vec3(self._y, self._y, self._z)
    @property
    def yzz(self) -> "vec3":
        return vec3(self._y, self._z, self._z)
    @property
    def zzz(self) -> "vec3":
        return vec3(self._z, self._z, self._z)
class vec4:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
            self._w = 0.0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> vec2:
        return vec2(self._x, self._x)
    @property
    def xy(self) -> vec2:
        return vec2(self._x, self._y)
    @property
    def xz(self) -> vec2:
        return vec2(self._x, self._z)
    @property
    def xw(self) -> vec2:
        return vec2(self._x, self._w)
    @property
    def yy(self) -> vec2:
        return vec2(self._y, self._y)
    @property
    def yz(self) -> vec2:
        return vec2(self._y, self._z)
    @property
    def yw(self) -> vec2:
        return vec2(self._y, self._w)
    @property
    def zz(self) -> vec2:
        return vec2(self._z, self._z)
    @property
    def zw(self) -> vec2:
        return vec2(self._z, self._w)
    @property
    def ww(self) -> vec2:
        return vec2(self._w, self._w)
    @property
    def xxx(self) -> vec3:
        return vec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> vec3:
        return vec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> vec3:
        return vec3(self._x, self._x, self._z)
    @property
    def xxw(self) -> vec3:
        return vec3(self._x, self._x, self._w)
    @property
    def xyy(self) -> vec3:
        return vec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> vec3:
        return vec3(self._x, self._y, self._z)
    @property
    def xyw(self) -> vec3:
        return vec3(self._x, self._y, self._w)
    @property
    def xzz(self) -> vec3:
        return vec3(self._x, self._z, self._z)
    @property
    def xzw(self) -> vec3:
        return vec3(self._x, self._z, self._w)
    @property
    def xww(self) -> vec3:
        return vec3(self._x, self._w, self._w)
    @property
    def yyy(self) -> vec3:
        return vec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> vec3:
        return vec3(self._y, self._y, self._z)
    @property
    def yyw(self) -> vec3:
        return vec3(self._y, self._y, self._w)
    @property
    def yzz(self) -> vec3:
        return vec3(self._y, self._z, self._z)
    @property
    def yzw(self) -> vec3:
        return vec3(self._y, self._z, self._w)
    @property
    def yww(self) -> vec3:
        return vec3(self._y, self._w, self._w)
    @property
    def zzz(self) -> vec3:
        return vec3(self._z, self._z, self._z)
    @property
    def zzw(self) -> vec3:
        return vec3(self._z, self._z, self._w)
    @property
    def zww(self) -> vec3:
        return vec3(self._z, self._w, self._w)
    @property
    def www(self) -> vec3:
        return vec3(self._w, self._w, self._w)
    @property
    def xxxx(self) -> "vec4":
        return vec4(self._x, self._x, self._x, self._x)
    @property
    def xxxy(self) -> "vec4":
        return vec4(self._x, self._x, self._x, self._y)
    @property
    def xxxz(self) -> "vec4":
        return vec4(self._x, self._x, self._x, self._z)
    @property
    def xxxw(self) -> "vec4":
        return vec4(self._x, self._x, self._x, self._w)
    @property
    def xxyy(self) -> "vec4":
        return vec4(self._x, self._x, self._y, self._y)
    @property
    def xxyz(self) -> "vec4":
        return vec4(self._x, self._x, self._y, self._z)
    @property
    def xxyw(self) -> "vec4":
        return vec4(self._x, self._x, self._y, self._w)
    @property
    def xxzz(self) -> "vec4":
        return vec4(self._x, self._x, self._z, self._z)
    @property
    def xxzw(self) -> "vec4":
        return vec4(self._x, self._x, self._z, self._w)
    @property
    def xxww(self) -> "vec4":
        return vec4(self._x, self._x, self._w, self._w)
    @property
    def xyyy(self) -> "vec4":
        return vec4(self._x, self._y, self._y, self._y)
    @property
    def xyyz(self) -> "vec4":
        return vec4(self._x, self._y, self._y, self._z)
    @property
    def xyyw(self) -> "vec4":
        return vec4(self._x, self._y, self._y, self._w)
    @property
    def xyzz(self) -> "vec4":
        return vec4(self._x, self._y, self._z, self._z)
    @property
    def xyzw(self) -> "vec4":
        return vec4(self._x, self._y, self._z, self._w)
    @property
    def xyww(self) -> "vec4":
        return vec4(self._x, self._y, self._w, self._w)
    @property
    def xzzz(self) -> "vec4":
        return vec4(self._x, self._z, self._z, self._z)
    @property
    def xzzw(self) -> "vec4":
        return vec4(self._x, self._z, self._z, self._w)
    @property
    def xzww(self) -> "vec4":
        return vec4(self._x, self._z, self._w, self._w)
    @property
    def xwww(self) -> "vec4":
        return vec4(self._x, self._w, self._w, self._w)
    @property
    def yyyy(self) -> "vec4":
        return vec4(self._y, self._y, self._y, self._y)
    @property
    def yyyz(self) -> "vec4":
        return vec4(self._y, self._y, self._y, self._z)
    @property
    def yyyw(self) -> "vec4":
        return vec4(self._y, self._y, self._y, self._w)
    @property
    def yyzz(self) -> "vec4":
        return vec4(self._y, self._y, self._z, self._z)
    @property
    def yyzw(self) -> "vec4":
        return vec4(self._y, self._y, self._z, self._w)
    @property
    def yyww(self) -> "vec4":
        return vec4(self._y, self._y, self._w, self._w)
    @property
    def yzzz(self) -> "vec4":
        return vec4(self._y, self._z, self._z, self._z)
    @property
    def yzzw(self) -> "vec4":
        return vec4(self._y, self._z, self._z, self._w)
    @property
    def yzww(self) -> "vec4":
        return vec4(self._y, self._z, self._w, self._w)
    @property
    def ywww(self) -> "vec4":
        return vec4(self._y, self._w, self._w, self._w)
    @property
    def zzzz(self) -> "vec4":
        return vec4(self._z, self._z, self._z, self._z)
    @property
    def zzzw(self) -> "vec4":
        return vec4(self._z, self._z, self._z, self._w)
    @property
    def zzww(self) -> "vec4":
        return vec4(self._z, self._z, self._w, self._w)
    @property
    def zwww(self) -> "vec4":
        return vec4(self._z, self._w, self._w, self._w)
    @property
    def wwww(self) -> "vec4":
        return vec4(self._w, self._w, self._w, self._w)
class dvec2:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0.0
            self._y = 0.0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> "dvec2":
        return dvec2(self._x, self._x)
    @property
    def xy(self) -> "dvec2":
        return dvec2(self._x, self._y)
    @property
    def yy(self) -> "dvec2":
        return dvec2(self._y, self._y)
class dvec3:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> dvec2:
        return dvec2(self._x, self._x)
    @property
    def xy(self) -> dvec2:
        return dvec2(self._x, self._y)
    @property
    def xz(self) -> dvec2:
        return dvec2(self._x, self._z)
    @property
    def yy(self) -> dvec2:
        return dvec2(self._y, self._y)
    @property
    def yz(self) -> dvec2:
        return dvec2(self._y, self._z)
    @property
    def zz(self) -> dvec2:
        return dvec2(self._z, self._z)
    @property
    def xxx(self) -> "dvec3":
        return dvec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> "dvec3":
        return dvec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> "dvec3":
        return dvec3(self._x, self._x, self._z)
    @property
    def xyy(self) -> "dvec3":
        return dvec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> "dvec3":
        return dvec3(self._x, self._y, self._z)
    @property
    def xzz(self) -> "dvec3":
        return dvec3(self._x, self._z, self._z)
    @property
    def yyy(self) -> "dvec3":
        return dvec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> "dvec3":
        return dvec3(self._y, self._y, self._z)
    @property
    def yzz(self) -> "dvec3":
        return dvec3(self._y, self._z, self._z)
    @property
    def zzz(self) -> "dvec3":
        return dvec3(self._z, self._z, self._z)
class dvec4:
    def __init__(self, *args):
        if len(args) == 1 and is_scalar(args[0]):
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
            self._w = 0.0
        else:
            raise NotImplementedError()
    @property
    def xx(self) -> dvec2:
        return dvec2(self._x, self._x)
    @property
    def xy(self) -> dvec2:
        return dvec2(self._x, self._y)
    @property
    def xz(self) -> dvec2:
        return dvec2(self._x, self._z)
    @property
    def xw(self) -> dvec2:
        return dvec2(self._x, self._w)
    @property
    def yy(self) -> dvec2:
        return dvec2(self._y, self._y)
    @property
    def yz(self) -> dvec2:
        return dvec2(self._y, self._z)
    @property
    def yw(self) -> dvec2:
        return dvec2(self._y, self._w)
    @property
    def zz(self) -> dvec2:
        return dvec2(self._z, self._z)
    @property
    def zw(self) -> dvec2:
        return dvec2(self._z, self._w)
    @property
    def ww(self) -> dvec2:
        return dvec2(self._w, self._w)
    @property
    def xxx(self) -> dvec3:
        return dvec3(self._x, self._x, self._x)
    @property
    def xxy(self) -> dvec3:
        return dvec3(self._x, self._x, self._y)
    @property
    def xxz(self) -> dvec3:
        return dvec3(self._x, self._x, self._z)
    @property
    def xxw(self) -> dvec3:
        return dvec3(self._x, self._x, self._w)
    @property
    def xyy(self) -> dvec3:
        return dvec3(self._x, self._y, self._y)
    @property
    def xyz(self) -> dvec3:
        return dvec3(self._x, self._y, self._z)
    @property
    def xyw(self) -> dvec3:
        return dvec3(self._x, self._y, self._w)
    @property
    def xzz(self) -> dvec3:
        return dvec3(self._x, self._z, self._z)
    @property
    def xzw(self) -> dvec3:
        return dvec3(self._x, self._z, self._w)
    @property
    def xww(self) -> dvec3:
        return dvec3(self._x, self._w, self._w)
    @property
    def yyy(self) -> dvec3:
        return dvec3(self._y, self._y, self._y)
    @property
    def yyz(self) -> dvec3:
        return dvec3(self._y, self._y, self._z)
    @property
    def yyw(self) -> dvec3:
        return dvec3(self._y, self._y, self._w)
    @property
    def yzz(self) -> dvec3:
        return dvec3(self._y, self._z, self._z)
    @property
    def yzw(self) -> dvec3:
        return dvec3(self._y, self._z, self._w)
    @property
    def yww(self) -> dvec3:
        return dvec3(self._y, self._w, self._w)
    @property
    def zzz(self) -> dvec3:
        return dvec3(self._z, self._z, self._z)
    @property
    def zzw(self) -> dvec3:
        return dvec3(self._z, self._z, self._w)
    @property
    def zww(self) -> dvec3:
        return dvec3(self._z, self._w, self._w)
    @property
    def www(self) -> dvec3:
        return dvec3(self._w, self._w, self._w)
    @property
    def xxxx(self) -> "dvec4":
        return dvec4(self._x, self._x, self._x, self._x)
    @property
    def xxxy(self) -> "dvec4":
        return dvec4(self._x, self._x, self._x, self._y)
    @property
    def xxxz(self) -> "dvec4":
        return dvec4(self._x, self._x, self._x, self._z)
    @property
    def xxxw(self) -> "dvec4":
        return dvec4(self._x, self._x, self._x, self._w)
    @property
    def xxyy(self) -> "dvec4":
        return dvec4(self._x, self._x, self._y, self._y)
    @property
    def xxyz(self) -> "dvec4":
        return dvec4(self._x, self._x, self._y, self._z)
    @property
    def xxyw(self) -> "dvec4":
        return dvec4(self._x, self._x, self._y, self._w)
    @property
    def xxzz(self) -> "dvec4":
        return dvec4(self._x, self._x, self._z, self._z)
    @property
    def xxzw(self) -> "dvec4":
        return dvec4(self._x, self._x, self._z, self._w)
    @property
    def xxww(self) -> "dvec4":
        return dvec4(self._x, self._x, self._w, self._w)
    @property
    def xyyy(self) -> "dvec4":
        return dvec4(self._x, self._y, self._y, self._y)
    @property
    def xyyz(self) -> "dvec4":
        return dvec4(self._x, self._y, self._y, self._z)
    @property
    def xyyw(self) -> "dvec4":
        return dvec4(self._x, self._y, self._y, self._w)
    @property
    def xyzz(self) -> "dvec4":
        return dvec4(self._x, self._y, self._z, self._z)
    @property
    def xyzw(self) -> "dvec4":
        return dvec4(self._x, self._y, self._z, self._w)
    @property
    def xyww(self) -> "dvec4":
        return dvec4(self._x, self._y, self._w, self._w)
    @property
    def xzzz(self) -> "dvec4":
        return dvec4(self._x, self._z, self._z, self._z)
    @property
    def xzzw(self) -> "dvec4":
        return dvec4(self._x, self._z, self._z, self._w)
    @property
    def xzww(self) -> "dvec4":
        return dvec4(self._x, self._z, self._w, self._w)
    @property
    def xwww(self) -> "dvec4":
        return dvec4(self._x, self._w, self._w, self._w)
    @property
    def yyyy(self) -> "dvec4":
        return dvec4(self._y, self._y, self._y, self._y)
    @property
    def yyyz(self) -> "dvec4":
        return dvec4(self._y, self._y, self._y, self._z)
    @property
    def yyyw(self) -> "dvec4":
        return dvec4(self._y, self._y, self._y, self._w)
    @property
    def yyzz(self) -> "dvec4":
        return dvec4(self._y, self._y, self._z, self._z)
    @property
    def yyzw(self) -> "dvec4":
        return dvec4(self._y, self._y, self._z, self._w)
    @property
    def yyww(self) -> "dvec4":
        return dvec4(self._y, self._y, self._w, self._w)
    @property
    def yzzz(self) -> "dvec4":
        return dvec4(self._y, self._z, self._z, self._z)
    @property
    def yzzw(self) -> "dvec4":
        return dvec4(self._y, self._z, self._z, self._w)
    @property
    def yzww(self) -> "dvec4":
        return dvec4(self._y, self._z, self._w, self._w)
    @property
    def ywww(self) -> "dvec4":
        return dvec4(self._y, self._w, self._w, self._w)
    @property
    def zzzz(self) -> "dvec4":
        return dvec4(self._z, self._z, self._z, self._z)
    @property
    def zzzw(self) -> "dvec4":
        return dvec4(self._z, self._z, self._z, self._w)
    @property
    def zzww(self) -> "dvec4":
        return dvec4(self._z, self._z, self._w, self._w)
    @property
    def zwww(self) -> "dvec4":
        return dvec4(self._z, self._w, self._w, self._w)
    @property
    def wwww(self) -> "dvec4":
        return dvec4(self._w, self._w, self._w, self._w)
